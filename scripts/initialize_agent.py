from swarmnode import SwarmClient

class KlyoteAgent:
    def __init__(self, api_key):
        """Initialize the Klyote Agent."""
        self.client = SwarmClient(api_key=api_key)

    def create_agent(self, agent_name, capabilities):
        """Create an AI agent."""
        response = self.client.create_node(name=agent_name, attributes=capabilities)
        return response

if __name__ == "__main__":
    import os
    API_KEY = os.getenv("SWARMNODE_API_KEY")
    if not API_KEY:
        raise ValueError("Please set the SWARMNODE_API_KEY environment variable.")

    klyote = KlyoteAgent(api_key=API_KEY)
    capabilities = {"sentience": True, "interaction": "adaptive"}
    klyote.create_agent("Klyote", capabilities)
