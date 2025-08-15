import networkx as nx
import matplotlib.pyplot as plt

# --- Load Graph from file ---
G = nx.read_edgelist(
    "Email-Enron.txt", 
    create_using=nx.Graph(), 
    nodetype=int
)

# --- Basic Info ---
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

# --- Top 10 nodes by degree ---
degree_dict = dict(G.degree())
top_10_nodes = sorted(degree_dict.items(), key=lambda x: x[1], reverse=True)[:10]
print("\nTop 10 most connected nodes (node_id, degree):")
for node, deg in top_10_nodes:
    print(node, deg)

# --- Degree Histogram ---
plt.figure(figsize=(8, 5))
plt.hist(degree_dict.values(), bins=50, color='skyblue', edgecolor='black')
plt.title("Degree Distribution")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.show()

# --- Graph Visualization (sample only) ---
sample_nodes = list(G.nodes())[:100]  # first 100 nodes only
sample_subgraph = G.subgraph(sample_nodes)

plt.figure(figsize=(8, 8))
nx.draw_networkx(sample_subgraph, node_size=50, with_labels=False)
plt.title("Sample Graph Visualization (100 nodes)")
plt.show()
