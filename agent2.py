"""
Generates a line chart of daily review sentiment counts for a given date range.
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import re
import numpy as np

def _parse_date_range(range_str: str):
    """Parse date range string into start/end dates (e.g., 'last 7 days' or 'YYYY-MM-DD to YYYY-MM-DD')."""
    range_str = range_str.strip().lower()
    if range_str.startswith("last"):
        days = int(re.findall(r"\d+", range_str)[0])
        end = datetime.now().replace(hour=23, minute=59, second=59, microsecond=0)
        start = end - timedelta(days=days)
        return start, end
    else:
        start_str, end_str = [part.strip() for part in range_str.split("to")]
        return pd.to_datetime(start_str), pd.to_datetime(end_str)

def plot_sentiment(
    date_range: str,
    csv_path: str = "reviews.csv",
    output_png: str = "sentiment_plot.png"
):
    try:
        # Load and clean review data
        df = pd.read_csv(
            csv_path,
            header=0,                # file *now* has a header row
            usecols=["rating_review", "review_full", "date"],
            dtype={"rating_review": "Int64"},
        )

        # parse the date exactly as before
        df["date"] = pd.to_datetime(df["date"], format="%d-%b-%y", errors="coerce")

        # Fallback date parsing
        def _safe_parse_date(x):
            try:
                return pd.to_datetime(x, format="%d-%b-%y", errors="coerce")
            except Exception:
                return pd.to_datetime(x, errors="coerce")

        df["date"] = df["date"].apply(_safe_parse_date)
        df = df.dropna(subset=["date", "rating_review"])
        df["rating_review"] = df["rating_review"].astype(int)

        # Convert ratings to sentiments
        def rating_to_sentiment(r):
            if r >= 4: return "Positive"
            elif r == 3: return "Neutral"
            else: return "Negative"

        df["sentiment"] = df["rating_review"].apply(rating_to_sentiment)

        # Filter by date range
        start_date, end_date = _parse_date_range(date_range)
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("No data found in the given date range.")
            return

        # Aggregate daily sentiment counts
        daily_counts = (
            filtered_df.groupby(["date", "sentiment"])
            .size()
            .unstack(fill_value=0)
            .asfreq("D", fill_value=0)
        )

        # Generate and save plot
        plt.figure(figsize=(10, 6))
        colors = {"Positive": "green", "Negative": "red", "Neutral": "blue"}
        for sentiment in daily_counts.columns:
            plt.plot(
                daily_counts.index,
                daily_counts[sentiment],
                marker="o",
                label=sentiment,
                color=colors[sentiment],
            )

        plt.title(f"Daily Review Sentiment\n{start_date.strftime('%b %d, %Y')} to {end_date.strftime('%b %d, %Y')}")
        plt.xlabel("Date")
        plt.ylabel("Number of Reviews")
        plt.legend(title="Sentiment")
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(output_png)
        print(f"Plot saved as '{output_png}'")

    except Exception as e:
        print(f"Error generating plot: {e}")