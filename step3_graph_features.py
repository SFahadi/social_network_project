import networkx as nx
import pandas as pd

# --- Load Graph ---
G = nx.read_edgelist(
    "Email-Enron.txt", 
    create_using=nx.Graph(), 
    nodetype=int
)

# --- Features Calculation ---
print("Calculating features...")

degree_dict = dict(G.degree())
clustering_dict = nx.clustering(G)
betweenness_dict = nx.betweenness_centrality(G, k=500, seed=42)  # sample for speed
pagerank_dict = nx.pagerank(G, alpha=0.85)

# --- Store in DataFrame ---
df = pd.DataFrame({
    "node": list(G.nodes()),
    "degree": [degree_dict[n] for n in G.nodes()],
    "clustering_coef": [clustering_dict[n] for n in G.nodes()],
    "betweenness": [betweenness_dict[n] for n in G.nodes()],
    "pagerank": [pagerank_dict[n] for n in G.nodes()]
})

# Save to CSV
df.to_csv("graph_features.csv", index=False)
print("✅ Features saved to graph_features.csv")
print(df.head())
