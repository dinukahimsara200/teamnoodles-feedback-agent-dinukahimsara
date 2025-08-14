"""
Interactive demo runner for SteamNoodles Feedback Agents
Prompts the user for a date range, then runs both agents.
"""

from agent1 import generate_response
from agent2 import plot_sentiment

def main():
    # --- Agent 1: single review demo -----------------------------------------
    print("\n--- Agent 1: Feedback Response ---")
    sample_review = "The ramen broth was lukewarm and service was a bit slow"
    print(f"Review: {sample_review}")
    print("Response:", generate_response(sample_review))

    # --- Agent 2: user-supplied date range -----------------------------------
    print("\n--- Agent 2: Sentiment Plot ---")
    date_range = input(
        "Enter date range (e.g. '2019-09-01 to 2020-09-01' or 'last 7 days'): "
    ).strip()
    plot_sentiment(date_range)

if __name__ == "__main__":
    main()