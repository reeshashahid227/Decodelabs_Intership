# Project 2 --- Data Classification Using AI

## 📌 Overview

This project demonstrates a complete machine learning classification
workflow using the **Iris dataset** and the **K-Nearest Neighbors
(KNN)** algorithm.

The objective is to train a classification model that predicts the
species of an Iris flower from its physical measurements.

The project covers data loading, data understanding, feature scaling,
train/test splitting, model training, prediction, evaluation,
visualization, and K-value experimentation.

------------------------------------------------------------------------

## 🎯 Objectives

-   Load and understand the Iris dataset
-   Separate features and target values
-   Apply feature scaling
-   Split the dataset into training and testing sets
-   Train a KNN classification model
-   Make predictions on unseen test data
-   Evaluate model performance
-   Compare different K values
-   Visualize the confusion matrix
-   Analyze accuracy and F1 score

------------------------------------------------------------------------

## 📊 Dataset

The project uses the built-in **Iris dataset** from Scikit-learn.

The dataset contains:

-   **150 samples**
-   **4 input features**
-   **3 target classes**

### Features

1.  Sepal Length
2.  Sepal Width
3.  Petal Length
4.  Petal Width

### Target Classes

-   Setosa
-   Versicolor
-   Virginica

------------------------------------------------------------------------

## 🔄 Project Workflow

``` text
Iris Dataset
     ↓
Data Understanding
     ↓
Separate Features (X) and Target (y)
     ↓
Feature Scaling
     ↓
Train/Test Split
     ↓
KNN Model
     ↓
Prediction
     ↓
Model Evaluation
     ↓
Confusion Matrix
     ↓
Test Different K Values
     ↓
Find Best K
```

------------------------------------------------------------------------

## 🤖 Algorithm Used

### K-Nearest Neighbors (KNN)

KNN is a supervised machine learning classification algorithm.

It predicts the class of a new data point by looking at its nearest
training examples.

For example, when:

``` text
K = 5
```

the model considers the **5 nearest neighbors** and uses their classes
to make the prediction.

------------------------------------------------------------------------

## ⚙️ Data Preprocessing

### Feature Scaling

`StandardScaler` is used to standardize the input features.

``` python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

Scaling is useful for KNN because KNN relies on distances between data
points.

### Train/Test Split

The dataset is divided into:

-   **80% training data**
-   **20% testing data**

For 150 samples:

``` text
Training samples: 120
Testing samples: 30
```

------------------------------------------------------------------------

## 📈 Model Evaluation

The model is evaluated using:

-   Accuracy
-   F1 Score
-   Classification Report
-   Confusion Matrix

### Initial Results

Using:

``` text
K = 5
```

the model achieved:

``` text
Accuracy: 93.33%
F1 Score: 93.27%
```

### K Value Experimentation

Different K values from **1 to 15** were tested.

The best result from the experiment was:

``` text
Best K: 1
Best Accuracy: 96.67%
```

> Note: The best K depends on the particular train/test split and
> experiment settings.

------------------------------------------------------------------------

## 📊 Visualizations

The project produces two main visualizations:

### 1. Confusion Matrix Heatmap

The confusion matrix shows how many samples were correctly and
incorrectly classified for each Iris class.

### 2. K Value vs Accuracy

This graph compares different K values with their corresponding accuracy
to identify the best-performing K.

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   **Python**
-   **Scikit-learn**
-   **Matplotlib**
-   **Seaborn**

------------------------------------------------------------------------

## 📦 Installation

Make sure Python is installed on your computer.

Install the required libraries:

``` bash
pip install scikit-learn matplotlib seaborn
```

------------------------------------------------------------------------

## ▶️ How to Run

Clone or download the repository and open the project folder.

Run:

``` bash
python project2_classification.py
```

The program will:

1.  Load the Iris dataset
2.  Display dataset information
3.  Scale the features
4.  Split the data
5.  Train the KNN model
6.  Make predictions
7.  Calculate accuracy and F1 score
8.  Display the classification report
9.  Display the confusion matrix
10. Test different K values
11. Show the best K and accuracy
12. Display the K vs Accuracy graph

------------------------------------------------------------------------

## 📁 Project Structure

``` text
Project2/
│
├── project2_classification.py
└── README.md
```

------------------------------------------------------------------------

## 🧠 What I Learned

Through this project, I practiced:

-   Understanding a classification dataset
-   Features and target variables
-   Supervised learning
-   Feature scaling
-   Train/test splitting
-   KNN classification
-   Model training
-   Making predictions
-   Accuracy evaluation
-   F1 score
-   Classification reports
-   Confusion matrices
-   Data visualization
-   Hyperparameter experimentation
-   Comparing different K values

------------------------------------------------------------------------

## 🚀 Future Improvements

Possible improvements include:

-   Try other classification algorithms
-   Compare KNN with Logistic Regression
-   Try Decision Trees
-   Try Random Forest
-   Use cross-validation
-   Tune more hyperparameters
-   Build a simple Streamlit interface

------------------------------------------------------------------------

