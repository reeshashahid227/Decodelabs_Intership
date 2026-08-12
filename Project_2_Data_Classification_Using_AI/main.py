# ============================================================
# PROJECT 2: DATA CLASSIFICATION USING AI
# Dataset: Iris
# Algorithm: K-Nearest Neighbors (KNN)
# ============================================================

# -----------------------------
# 1. IMPORT LIBRARIES
# -----------------------------

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import (
    accuracy_score,
    f1_score,
    confusion_matrix,
    classification_report
)


# -----------------------------
# 2. LOAD DATASET
# -----------------------------

iris = load_iris()

X = iris.data
y = iris.target

print("=" * 50)
print("IRIS DATASET")
print("=" * 50)

print("Dataset shape:", X.shape)
print("Target shape:", y.shape)

print("\nFeatures:")
for feature in iris.feature_names:
    print("-", feature)

print("\nClasses:")
for class_name in iris.target_names:
    print("-", class_name)


# -----------------------------
# 3. CHECK DATA
# -----------------------------

print("\nFirst 5 samples:")
print(X[:5])

print("\nFirst 5 target values:")
print(y[:5])


# -----------------------------
# 4. FEATURE SCALING
# -----------------------------

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print("\nFeature scaling completed.")


# -----------------------------
# 5. TRAIN / TEST SPLIT
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])


# -----------------------------
# 6. TRAIN KNN MODEL
# -----------------------------

k = 5

model = KNeighborsClassifier(
    n_neighbors=k
)

model.fit(X_train, y_train)

print("\nKNN model trained.")
print("K =", k)


# -----------------------------
# 7. MAKE PREDICTIONS
# -----------------------------

y_pred = model.predict(X_test)

print("\nPredictions:")
print(y_pred)


# -----------------------------
# 8. ACCURACY
# -----------------------------

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\nAccuracy:")
print(accuracy)


# -----------------------------
# 9. F1 SCORE
# -----------------------------

f1 = f1_score(
    y_test,
    y_pred,
    average="weighted"
)

print("\nWeighted F1 Score:")
print(f1)


# -----------------------------
# 10. CLASSIFICATION REPORT
# -----------------------------

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=iris.target_names
    )
)


# -----------------------------
# 11. CONFUSION MATRIX
# -----------------------------

cm = confusion_matrix(
    y_test,
    y_pred
)

print("\nConfusion Matrix:")
print(cm)


# -----------------------------
# 12. CONFUSION MATRIX GRAPH
# -----------------------------

plt.figure(figsize=(7, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=iris.target_names,
    yticklabels=iris.target_names
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("KNN Confusion Matrix")

plt.tight_layout()
plt.show()


# -----------------------------
# 13. TEST DIFFERENT K VALUES
# -----------------------------

k_values = range(1, 16)

accuracies = []

for k in k_values:

    knn = KNeighborsClassifier(
        n_neighbors=k
    )

    knn.fit(
        X_train,
        y_train
    )

    predictions = knn.predict(
        X_test
    )

    acc = accuracy_score(
        y_test,
        predictions
    )

    accuracies.append(acc)


# -----------------------------
# 14. DISPLAY K RESULTS
# -----------------------------

print("\n" + "=" * 50)
print("K VALUE COMPARISON")
print("=" * 50)

for k, acc in zip(k_values, accuracies):

    print(
        f"K = {k:2d}  |  Accuracy = {acc:.4f}"
    )


# -----------------------------
# 15. FIND BEST K
# -----------------------------

best_index = accuracies.index(
    max(accuracies)
)

best_k = list(k_values)[best_index]

best_accuracy = accuracies[best_index]

print("\nBest K:", best_k)
print("Best Accuracy:", best_accuracy)


# -----------------------------
# 16. K VS ACCURACY GRAPH
# -----------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    k_values,
    accuracies,
    marker="o"
)

plt.xlabel("K Value")
plt.ylabel("Accuracy")
plt.title("K Value vs Accuracy")

plt.xticks(
    list(k_values)
)

plt.grid(True)

plt.tight_layout()
plt.show()


# -----------------------------
# 17. FINAL SUMMARY
# -----------------------------

print("\n" + "=" * 50)
print("PROJECT SUMMARY")
print("=" * 50)

print("Dataset       : Iris")
print("Algorithm     : K-Nearest Neighbors (KNN)")
print("Train samples :", X_train.shape[0])
print("Test samples  :", X_test.shape[0])
print("Initial K     :", 5)
print("Accuracy      :", accuracy)
print("F1 Score      :", f1)
print("Best K        :", best_k)
print("Best Accuracy :", best_accuracy)

print("\nProject completed successfully!")