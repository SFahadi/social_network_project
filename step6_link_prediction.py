import networkx as nx
import pandas as pd
import itertools

# --- Load graph from file ---
G = nx.read_edgelist("Email-Enron.txt", nodetype=int)

print("✅ Graph Loaded")
print(f"Nodes: {G.number_of_nodes()}, Edges: {G.number_of_edges()}")

# --- Example: Adamic-Adar Index ---
print("\n🔍 Calculating Adamic-Adar Scores... (This may take a while for big graphs)")

# We'll pick only a small sample of non-connected node pairs to keep it fast
non_edges = list(itertools.islice(nx.non_edges(G), 5000))  # only first 5000 non-edges
scores = nx.adamic_adar_index(G, non_edges)

# --- Convert to DataFrame ---
predictions = []
for u, v, score in scores:
    predictions.append((u, v, score))

df_pred = pd.DataFrame(predictions, columns=["node1", "node2", "adamic_adar_score"])

# --- Sort by highest probability ---
df_pred = df_pred.sort_values(by="adamic_adar_score", ascending=False)

# Save predictions
df_pred.to_csv("link_predictions.csv", index=False)
print("✅ Predictions saved to link_predictions.csv")

# --- Show top 10 predicted links ---
print("\nTop 10 Predicted Future Links:")
print(df_pred.head(10))
