def call_agent_api(agent, endpoint, params):
    """Send a custom request to the agent API."""
    response = agent.api_call(endpoint, params)
    return response
