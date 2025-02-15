# -*- coding: utf-8 -*-
"""Copy of random

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zwT8zB6YFQVK5V1CBtO3gGw9uapXxY-5
"""







# Code source: Gaël Varoquaux
# Modified for documentation by Jaques Grobler
# License: BSD 3 clause
import pandas as pd

import numpy as np
from sklearn.preprocessing import MinMaxScaler


from sklearn.ensemble import RandomForestRegressor

train=pd.read_csv('/content/train.csv')
test=pd.read_csv('/content/test.csv')
m=test['id']

train.drop('id',axis=1,inplace=True) #drop irrelevent column
test.drop('id',axis=1,inplace=True) #drop irrelevent column

y = train["Response"]
x=train.drop('Response',axis=1)
x

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report


train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")


X = train_data.drop(columns=["id", "Response"])
y = train_data["Response"]


X = X.astype(float)
test_data = test_data.astype(float)


if "bmi" in X.columns and "age" in X.columns:
    X["BMI_Age_Ratio"] = X["bmi"] / (X["age"] + 1)
    test_data["BMI_Age_Ratio"] = test_data["bmi"] / (test_data["age"] + 1)


X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)
X_test = test_data.drop(columns=["id"])
X_test_scaled = scaler.transform(X_test)


tree = DecisionTreeClassifier(
    criterion="gini",
    max_depth=10,
    min_samples_split=5,
    min_samples_leaf=3,
    random_state=42
)

tree.fit(X_train_scaled, y_train)


y_val_pred = tree.predict(X_val_scaled)
val_accuracy = accuracy_score(y_val, y_val_pred)
print(f"Validation Accuracy: {val_accuracy:.4f}")
print("\nClassification Report:")
print(classification_report(y_val, y_val_pred))


test_predictions = tree.predict(X_test_scaled)


output = pd.DataFrame({"id": test_data["id"].astype(int), "Response": test_predictions})
output.to_csv("submission_tree.csv", index=False)
print("\nPredictions saved to submission_tree.csv")
model = RandomForestRegressor(max_depth=8,n_estimators=206,random_state=110)
model.fit(x,y)

y_predict = model.predict(test)
y_predict

#Convert into a csv file
c=pd.DataFrame(y_predict)
c.rename(columns={0: "smoking"}, inplace=True)
c.insert(0, 'id',m)
c.to_csv('predictied.csv',index=False)







