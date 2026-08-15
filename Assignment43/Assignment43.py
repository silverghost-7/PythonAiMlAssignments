import math
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler

#Variables
Weather = "Weather"
Temperature = "Temperature"
Play = "Play"

Weather_values = {"Sunny":0, "Overcast":1,"Rainy":2}
Temperature_values = {"Hot":0, "Cool":1, "Mild":2}


def CalculateEuclideanDistance(p1, p2):
    return math.sqrt(((p1[Weather]-p2[Weather])**2) + ((p1[Temperature]-p2[Temperature])**2))

def KNNClassifierX(k = 3):
    Data = [
        {Weather : Weather_values["Sunny"], Temperature : Temperature_values["Hot"], Play : "No"},
        {Weather : Weather_values["Sunny"], Temperature : Temperature_values["Hot"], Play : "No"},
        {Weather : Weather_values["Overcast"], Temperature : Temperature_values["Hot"], Play : "Yes"},
        {Weather : Weather_values["Rainy"], Temperature : Temperature_values["Mild"], Play : "Yes"},
        {Weather : Weather_values["Rainy"], Temperature : Temperature_values["Cool"], Play : "Yes"},
        {Weather : Weather_values["Rainy"], Temperature : Temperature_values["Cool"], Play : "No"},
        {Weather : Weather_values["Overcast"], Temperature : Temperature_values["Cool"], Play : "Yes"},
        {Weather : Weather_values["Sunny"], Temperature : Temperature_values["Mild"], Play : "No"},
        {Weather : Weather_values["Sunny"], Temperature : Temperature_values["Cool"], Play : "Yes"},
        {Weather : Weather_values["Rainy"], Temperature : Temperature_values["Mild"], Play : "Yes"}
    ]

    df = pd.DataFrame(Data, columns=[Weather,Temperature,Play])
    X = df.drop(columns=[Play])
    Y = df[Play]

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42,stratify=Y)

    Model = KNeighborsClassifier(n_neighbors=k)
    Model = Model.fit(X_train,Y_train)
    Y_Pred = Model.predict(X_test)
    Accuracy = accuracy_score(Y_Pred,Y_test)
    return Accuracy

def main():
    for i in range(5):
        k = (2*i)+1
        Prediction = KNNClassifierX()
        print(f"K = {k} -> Predicted Result: {Prediction}")

if (__name__=="__main__"):
    main()