def post_social_content(agent, api):
    """Generate and post content to social platforms."""
    prompt = "Create a motivational quote for today."
    content = agent.process_request(prompt)
    api.update_status(content)
