import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import random

# --- Load data ---
df = pd.read_csv("graph_features.csv")

# --- Feature Importance Plot ---
importances = {
    "degree": 0.714687,
    "pagerank": 0.201069,
    "betweenness": 0.078165,
    "clustering_coef": 0.006080
}
plt.figure(figsize=(6, 4))
plt.bar(importances.keys(), importances.values(), color="skyblue")
plt.title("Feature Importance")
plt.ylabel("Importance Score")
plt.show()

# --- Degree Distribution ---
plt.figure(figsize=(6, 4))
plt.hist(df["degree"], bins=50, color="orange")
plt.title("Degree Distribution")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.show()

# --- Sample Graph Visualization ---
print("Loading full graph for visualization...")
G = nx.read_edgelist("Email-Enron.txt", nodetype=int)

# Sample subgraph
sample_nodes = random.sample(list(G.nodes()), 300)
H = G.subgraph(sample_nodes)

plt.figure(figsize=(8, 6))
pos = nx.spring_layout(H, seed=42)
nx.draw(H, pos, node_size=50, node_color="lightgreen", edge_color="gray", with_labels=False)
plt.title("Sample Visualization of Enron Email Network")
plt.show()
