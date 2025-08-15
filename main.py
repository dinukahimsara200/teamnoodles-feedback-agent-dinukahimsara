"""
Interactive demo runner for SteamNoodles Feedback Agents
Prompts the user for a date range, runs both agents, and displays the sentiment plot.
"""

from agent1 import generate_response
from agent2 import plot_sentiment
import matplotlib.pyplot as plt
import os

def main():
    # --- Agent 1: single review demo 
    print("\n" + "="*50)
    print("Agent 1: Automated Review Response")
    print("="*50)
    review = input(
        "\nEnter a restaurant review (e.g. 'Great cocktails and friendly service!')\n> "
    )
    print(f"\nGenerating response for:\n'{review}'")
    print("\nResponse:", generate_response(review))

    # --- Agent 2: user-supplied date range 
    print("\n" + "="*50)
    print("Agent 2: Sentiment Analysis Visualizer")
    print("="*50)
    print("\nAvailable date formats:")
    print("- Specific range: '2019-03-31 to 2020-03-31'")
    print("- Relative range: 'last 7 days'")
    
    date_range = input("\nEnter date range\n> ").strip()
    output_file = "sentiment_plot.png"
    
    plot_sentiment(date_range, output_png=output_file)
    
    # Display the generated plot
    if os.path.exists(output_file):
        print("\nDisplaying sentiment plot...")
        img = plt.imread(output_file)
        plt.figure(figsize=(10, 6))
        plt.imshow(img)
        plt.axis('off')  # Hide axes
        plt.tight_layout()
        plt.show()
    else:
        print("\nError: Plot could not be generated.")

if __name__ == "__main__":
    main()