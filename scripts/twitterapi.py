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

# Post a tweet
def post_tweet(api, content):
    """Post a tweet using the Twitter API."""
    try:
        tweet = api.update_status(content)
        print(f"Tweet posted successfully: {tweet.text}")
    except Exception as e:
        print(f"Error posting tweet: {e}")

# Generate tweet content from Klyote agent
def generate_tweet(agent):
    """Generate a tweet using the Klyote agent's intelligence."""
    try:
        print("Generating tweet content using Klyote agent...")
        prompt = "Share an inspiring thought for today."
        response = agent.process_request(prompt)
        return response
    except Exception as e:
        print(f"Error generating tweet content: {e}")
        return None

if __name__ == "__main__":
    # Initialize Twitter API
    print("Initializing Twitter API...")
    twitter_api = initialize_twitter_api()

    # Initialize Klyote Agent
    print("Initializing Klyote agent...")
    api_key = os.getenv("SWARMNODE_API_KEY")
    if not api_key:
        raise ValueError("Please set the SWARMNODE_API_KEY environment variable.")

    klyote_agent = KlyoteAgent(api_key=api_key)

    # Generate and post tweet
    tweet_content = generate_tweet(klyote_agent)
    if tweet_content:
        post_tweet(twitter_api, tweet_content)
