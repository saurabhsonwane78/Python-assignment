from graphviz import Digraph

# Create a Directed Graph
graph = Digraph('Flowchart', format='png', engine='dot')

# Define nodes
nodes = ['A', 'B', 'C', 'D', 'E']

# Define edges
edges = [('A', 'B'), ('B', 'D'), ('C', 'E'), ('D', 'E'), ('A', 'E')]

# Add nodes to the graph
for node in nodes:
    graph.node(node)

# Add edges to the graph
for edge in edges:
    graph.edge(edge[0], edge[1])

# Save the graph to a file
graph.render(filename='flowchart', cleanup=True, format='png', directory='.')

print("Flowchart created successfully.")
