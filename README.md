# Enron Email Network Analysis & Link Prediction

This project analyzes the **Enron Email Dataset** using Network Analysis, Machine Learning, and Link Prediction techniques.  
The workflow is divided into 7 steps, from loading the dataset to predicting future links in the network.

---

## 📂 Steps Overview

1. **Load Graph (step1_load_graph.py)**  
   - Load the dataset (`Email-Enron.txt`) into a NetworkX graph.
   - Show basic stats: nodes, edges, sample edges.

2. **Graph Analysis (step2_graph_analysis.py)**  
   - Calculate top connected nodes.
   - Plot degree distribution.
   - Visualize a sample network.

3. **Feature Extraction (step3_graph_features.py)**  
   - Calculate:
     - Degree
     - Clustering Coefficient
     - Betweenness Centrality
     - PageRank
   - Save to `graph_features.csv`.

4. **Machine Learning Model (step4_ml_model.py)**  
   - Train a Random Forest Classifier to identify highly connected nodes.
   - Show classification report & feature importance.

5. **Visualization (step5_visualization.py)**  
   - Feature importance plot.
   - Degree distribution histogram.
   - Sample network visualization.

6. **Link Prediction (step6_link_prediction.py)**  
   - Use **Adamic-Adar Index** to score potential future links.
   - Save results to `link_predictions.csv`.

7. **Predicted Links Visualization (step7_visualization.py)**  
   - Draw original graph + highlight predicted links (red dashed edges).
   - Save to `graph_with_predictions.png`.

---

## 📦 Requirements

- Python 3.8+
- Libraries:
  ```bash
  pip install networkx pandas matplotlib scikit-learn

How to Run

Clone this repository:

git clone https://github.com/yourusername/enron-email-analysis.git
cd enron-email-analysis


Place the dataset file Email-Enron.txt in the project folder.

Run each step sequentially:

python step1_load_graph.py
python step2_graph_analysis.py
python step3_graph_features.py
python step4_ml_model.py
python step5_visualization.py
python step6_link_prediction.py
python step7_visualization.py


Check Outputs:

CSV files: graph_features.csv, link_predictions.csv

PNG graphs: graph_with_predictions.png, degree distribution plots, etc.
