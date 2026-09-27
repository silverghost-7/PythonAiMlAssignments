import pandas as pd

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report, confusion_matrix,f1_score

def main():
    # Step 1 : load dataset
    df = load_breast_cancer(as_frame=True).frame
    print(df.shape)
    print("First few reacords:")
    print(df.head())

    # Step 2 : Separate features and labels
    X = df.drop("target", axis=1)
    Y = df["target"]
    print("X shape:",X.shape)
    print("Y shape:",Y.shape)

    # Step 3 : Split dataset for training and testing
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    # Step 4 : Scale features
    scalar = StandardScaler()
    X_train = scalar.fit_transform(X_train)
    X_test = scalar.fit_transform(X_test)

    # Step 5 : Create model
    model = LogisticRegression(max_iter=1000)

    # Step 6 : Train model
    model = model.fit(X_train, Y_train)

    # Step 7 : Test model
    Y_pred = model.predict(X_test)

    # Step 8 : Evaluate the model
    print("Accuracy: ",accuracy_score(Y_test,Y_pred))
    print("Confusion matrix: \n",confusion_matrix(Y_test,Y_pred))
    print(f"Binary F1-Score:",f1_score(Y_test,Y_pred))


if (__name__=="__main__"):
    main()