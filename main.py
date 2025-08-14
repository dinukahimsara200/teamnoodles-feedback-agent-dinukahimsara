"""
Tests both agents with sample inputs:
- Agent 1: Generates a response to a restaurant review.
- Agent 2: Plots sentiment trends for a date range.
"""

from agent1 import generate_response
from agent2 import plot_sentiment

if __name__ == "__main__":
    # Test Agent 1 (Review Responder)
    print("\n--- Agent 1 Demo: Feedback Response ---")
    sample_review = "The ramen broth was lukewarm and service was a bit slow"
    print("Review:", sample_review)
    print("Response:", generate_response(sample_review))

    # Test Agent 2 (Sentiment Visualizer)
    print("\n--- Agent 2 Demo: Sentiment Plot ---")
    plot_sentiment("2020-09-01 to 2020-10-08")