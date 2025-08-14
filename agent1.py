"""
Automated restaurant feedback responder.  
Reads a review, detects sentiment (positive/neutral/negative),  
and generates a polite reply using Groq + LangChain.  
"""

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def generate_response(review_text: str) -> str:
    try:
        groq_api_key = os.getenv("GROQ_API_KEY")
        if not groq_api_key:
            return "Error: GROQ_API_KEY not found in .env file"

        # Set up Groq LLM with Llama3
        llm = ChatGroq(
            temperature=0.3,
            model_name="llama3-70b-8192",
            groq_api_key=groq_api_key
        )

        # Classify review sentiment (POSITIVE/NEGATIVE/NEUTRAL)
        sentiment_prompt = PromptTemplate(
            template=(
                "Classify the following restaurant review as POSITIVE, NEGATIVE, or NEUTRAL.\n"
                "Review: {review}\n"
                "Reply with exactly one word in uppercase:"
            ),
            input_variables=["review"]
        )
        sentiment_chain = sentiment_prompt | llm | StrOutputParser()

        # Generate a manager's response based on sentiment
        response_prompt = PromptTemplate(
            template=(
                "You are the manager of SteamNoodles. "
                "Write a single polite sentence responding to this {sentiment} review:\n"
                "Review: {review}"
            ),
            input_variables=["sentiment", "review"]
        )
        response_chain = (
            RunnablePassthrough.assign(sentiment=sentiment_chain)
            | response_prompt
            | llm
            | StrOutputParser()
        )

        return response_chain.invoke({"review": review_text})

    except Exception as e:
        return f"Error: {e}"