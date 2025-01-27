"""
Example 3: Personalized Recommendations
"""

from langchain.agents import initialize_agent, Tool

# User preferences mock data
user_preferences_data = {
    "1234": {"favorite_genres": ["Action", "Sci-Fi"], "favorite_actors": ["Tom Cruise"]}
}

# Tools
def user_preference_tool(user_id: str):
    return user_preferences_data.get(user_id, "No preferences found.")

def recommendation_tool(user_preferences):
    if not user_preferences:
        return "No preferences available for recommendations."
    return "Based on your preferences, we recommend 'Inception' and 'The Matrix'."

tools = [
    Tool(name="User Preferences", func=user_preference_tool, description="Retrieve user preferences."),
    Tool(name="Recommendation Generator", func=recommendation_tool, description="Generate recommendations.")
]

# Initialize the agent
agent = initialize_agent(tools, OpenAI(temperature=0.7), agent="zero-shot-react-description", verbose=True)

# Test the agent
user_id = "1234"
response = agent.run(f"Generate recommendations for user ID {user_id}.")
print(response)
