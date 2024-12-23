from swarmnode import SwarmClient

class KlyoteAgent:
    def __init__(self, api_key):
        """
        Initialize the Klyote Agent using the SwarmNode SDK.
        :param api_key: SwarmNode API key for authentication.
        """
        self.client = SwarmClient(api_key=api_key)

    def create_agent(self, agent_name, capabilities):
        """
        Create a Klyote agent with the specified name and capabilities.
        :param agent_name: The name of the agent to create.
        :param capabilities: A dictionary defining the agent's capabilities.
        :return: Response from the SwarmNode SDK.
        """
        try:
            response = self.client.create_node(
                name=agent_name,
                attributes=capabilities
            )
            print(f"Agent '{agent_name}' created successfully!")
            return response
        except Exception as e:
            print(f"Error creating agent: {e}")
            return None

if __name__ == "__main__":
    # Load your API key from environment variables or configuration
    import os
    
    API_KEY = os.getenv("SWARMNODE_API_KEY")
    if not API_KEY:
        raise ValueError("Please set the SWARMNODE_API_KEY environment variable.")

    # Initialize the Klyote Agent
    klyote_agent = KlyoteAgent(api_key=API_KEY)

    # Define agent capabilities
    capabilities = {
        "sentience": True,
        "learning_rate": "adaptive",
        "interaction_modes": ["text", "voice"],
        "processing_power": "high"
    }

    # Create the agent
    agent_name = "Klyote"
    response = klyote_agent.create_agent(agent_name, capabilities)

    if response:
        print("Agent Details:", response)
