import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler

def PrintHeader(header):
    border = "-"*60
    print(border)
    print(header)
    print(border)

def KNNClassifier(DataPath):
    # Step 1 : Load data from path
    PrintHeader("Step 1 : Load data from path")
    df = pd.read_csv(DataPath)
    print("Some entries in dataset:")
    print(df.head(5))

    #Step 2 : Clean dataset
    PrintHeader("Step 2 : Clean dataset")
    df.dropna(inplace=True)     #remove entire row if any of the cell value is empty
    print(df.shape)
    print("Total records:",df.shape[0])
    print("Total columns:",df.shape[1])

    # Step 3 : Separate Independent and dependent variables
    PrintHeader("Step 3 : Separate Independent and dependent variables")
    X = df.drop(columns=["Class"])
    Y = df["Class"]

    print("Shape X:",X.shape)
    print("Shape Y:",Y.shape)
    print("Input columns:",X.columns.tolist())
    print("Output column: Class")

    # Step 4 : Split dataset for training and testing
    PrintHeader("Step 4 : Split dataset for training and testing")
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)
    print("Details of training and testing data:")
    print("X_train:",X_train.shape)
    print("X_test:",X_test.shape)
    print("Y_train:",Y_train.shape)
    print("Y_test:",Y_test.shape)

    # Step 5 : Feature scaling
    PrintHeader("Step 5 : Feature scaling")
    scalar = StandardScaler()
    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)
    print("Feature scaling done")

    # Step 6 : Build model
    PrintHeader("Step 6 : Build model")
    Model = KNeighborsClassifier(n_neighbors=5)
    print("Classificaiton model created")

    # Step 7 : Train model
    PrintHeader("Step 7 : Train model")
    Model = Model.fit(X_train_scaled,Y_train)
    print("Model trained with scaled dataset")

    # Step 8 : Test model
    PrintHeader("Step 7 : Test model and check accuracy")
    Y_pred = Model.predict(X_test_scaled)
    accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuracy:",accuracy)


def main():
    KNNClassifier("WinePredictor.csv")

if (__name__=="__main__"):
    main()