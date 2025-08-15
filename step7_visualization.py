import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import random

# Load original graph
G = nx.read_edgelist("Email-Enron.txt", nodetype=int)

# Load predictions from Step 6
pred_df = pd.read_csv("link_predictions.csv")

# Pick top 20 predicted edges
top_preds = pred_df.head(20)
pred_edges = [(row["node1"], row["node2"]) for _, row in top_preds.iterrows()]

# ✅ Get all nodes involved in predictions + some random sample for context
pred_nodes = set([n for edge in pred_edges for n in edge])
extra_nodes = random.sample(list(G.nodes()), 80)  # extra 80 random nodes
sub_nodes = list(pred_nodes.union(extra_nodes))

# Create subgraph
G_sub = G.subgraph(sub_nodes)

# Positions for plotting
pos = nx.spring_layout(G_sub, seed=42)

# Draw normal edges (blue)
nx.draw_networkx_edges(G_sub, pos, edgelist=list(G_sub.edges()), 
                       width=0.5, alpha=0.5, edge_color='blue')

# Draw predicted edges (red dashed)
nx.draw_networkx_edges(G_sub, pos, edgelist=pred_edges, 
                       edge_color='red', style='dashed', width=1.5)

# Draw nodes
nx.draw_networkx_nodes(G_sub, pos, node_size=80, node_color='skyblue', alpha=0.9)

plt.title("Email Network (Sample) with Predicted Future Links", fontsize=14)
plt.axis('off')
plt.tight_layout()
plt.savefig("graph_with_predictions.png", dpi=300)
plt.show()

print("✅ Visualization saved as graph_with_predictions.png (sample version)")
