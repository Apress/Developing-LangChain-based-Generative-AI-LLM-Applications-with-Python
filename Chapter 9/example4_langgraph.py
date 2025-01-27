"""
Example 4: Creating a Simple LangGraph
"""

from langchain.graph import LangGraph, Node

# Define the nodes
node1 = Node(name="GreetUser", action=lambda: "Hello! How can I assist you with your travel plans today?")
node2 = Node(name="GetDestination", action=lambda user_input: f"{user_input} sounds like a fantastic destination.")
node3 = Node(name="SuggestActivities", action=lambda: "Here are some activities: visiting museums, exploring nature trails.")

# Create the LangGraph
travel_graph = LangGraph()
travel_graph.add_node(node1)
travel_graph.add_node(node2)
travel_graph.add_node(node3)

# Define the edges
travel_graph.add_edge("GreetUser", "GetDestination")
travel_graph.add_edge("GetDestination", "SuggestActivities")

# Test the graph
response = travel_graph.execute("GreetUser", "Hawaii")
print(response)
