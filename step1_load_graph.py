import networkx as nx

# اپنے data file کا path یہاں دو
file_path = "Email-Enron.txt"

# Graph object create کریں
G = nx.Graph()  # undirected graph

# File read کریں
with open(file_path, 'r') as f:
    for line in f:
        if line.startswith("#") or line.strip() == "":
            continue  # skip comments or empty lines
        src, dst = map(int, line.strip().split())
        G.add_edge(src, dst)

# Basic information
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

# کچھ sample nodes دکھاؤ
print("First 10 nodes:", list(G.nodes())[:10])
print("First 10 edges:", list(G.edges())[:10])
