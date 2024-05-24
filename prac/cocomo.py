import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Define tasks and dependencies
tasks = {
    'T1': {'duration': 10, 'dependencies': [], 'layer': 0},
    'T2': {'duration': 15, 'dependencies': ['T1'], 'layer': 1},
    'T3': {'duration': 10, 'dependencies': ['T1', 'T2'], 'layer': 1},
    'T4': {'duration': 20, 'dependencies': [], 'layer': 0},
    'T5': {'duration': 10, 'dependencies': [], 'layer': 0},
    'T6': {'duration': 15, 'dependencies': ['T3', 'T4'], 'layer': 1},
    'T7': {'duration': 20, 'dependencies': ['T3'], 'layer': 1},
    'T8': {'duration': 35, 'dependencies': ['T7'], 'layer': 2},
    'T9': {'duration': 15, 'dependencies': ['T6'], 'layer': 2},
    'T10': {'duration': 5, 'dependencies': ['T5', 'T9'], 'layer': 3},
    'T11': {'duration': 10, 'dependencies': ['T9'], 'layer': 3},
    'T12': {'duration': 20, 'dependencies': ['T10', 'T11'], 'layer': 4},
    'T13': {'duration': 35, 'dependencies': ['T3', 'T4'], 'layer': 2},
    'T14': {'duration': 10, 'dependencies': ['T8', 'T9'], 'layer': 3},
    'T15': {'duration': 20, 'dependencies': ['T12', 'T14'], 'layer': 5},
    'T16': {'duration': 10, 'dependencies': ['T15'], 'layer': 6}
}

# Add nodes and edges to the graph
for task, info in tasks.items():
    G.add_node(task, duration=info['duration'], layer=info['layer'])
    for dependency in info['dependencies']:
        G.add_edge(dependency, task)

# Position nodes using multipartite layout
pos = nx.multipartite_layout(G, subset_key="layer")

# Draw the network graph
plt.figure(figsize=(15, 10))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=7000, edge_color='k', font_size=10, font_color='black')
labels = {node: f"{node}\n(Duration: {info['duration']} days)" for node, info in tasks.items()}
nx.draw_networkx_labels(G, pos, labels=labels)
plt.title('Activity Chart')
plt.show()