import os
import tweepy
from klyote import KlyoteAgent

# Initialize Twitter API client
def initialize_twitter_api():
    """Initialize the Twitter API client using environment variables."""
    api_key = os.getenv("TWITTER_API_KEY")
    api_secret = os.getenv("TWITTER_API_SECRET")
    access_token = os.getenv("TWITTER_ACCESS_TOKEN")
    access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

    if not all([api_key, api_secret, access_token, access_token_secret]):
        raise ValueError("Please set all required Twitter API environment variables.")

    auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
    return tweepy.API(auth)

# Test the Twitter API
def test_twitter_api(api):
    """Test the Twitter API by fetching the authenticated user's details."""
    try:
        user = api.verify_credentials()
        if user:
            print(f"Twitter API authenticated as {user.screen_name}")
        else:
            print("Failed to authenticate Twitter API.")
    except Exception as e:
        print(f"Error testing Twitter API: {e}")

# Sentient test for Klyote agent
def sentient_test(agent):
    """Run a basic sentience test on the Klyote agent."""
    try:
        print("Running sentient test on Klyote agent...")
        question = "What is the meaning of existence?"
        response = agent.process_request(question)
        print(f"Question: {question}")
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error during sentient test: {e}")

if __name__ == "__main__":
    # Initialize Twitter API
    print("Initializing Twitter API...")
    twitter_api = initialize_twitter_api()

    # Test Twitter API
    test_twitter_api(twitter_api)

    # Initialize Klyote Agent
    print("Initializing Klyote agent...")
    api_key = os.getenv("SWARMNODE_API_KEY")
    if not api_key:
        raise ValueError("Please set the SWARMNODE_API_KEY environment variable.")

    klyote_agent = KlyoteAgent(api_key=api_key)

    # Run sentient test
    sentient_test(klyote_agent)
