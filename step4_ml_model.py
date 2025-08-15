import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# --- Load Data ---
df = pd.read_csv("graph_features.csv")

# --- Create Target Column ---
avg_degree = df["degree"].mean()
df["highly_connected"] = (df["degree"] > avg_degree).astype(int)

# Features and Target
X = df[["degree", "clustering_coef", "betweenness", "pagerank"]]
y = df["highly_connected"]

# --- Train/Test Split ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# --- Train Model ---
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# --- Predictions ---
y_pred = model.predict(X_test)

# --- Report ---
print("Classification Report:\n", classification_report(y_test, y_pred))

# --- Feature Importance ---
importances = pd.Series(model.feature_importances_, index=X.columns)
print("\nFeature Importances:")
print(importances.sort_values(ascending=False))
