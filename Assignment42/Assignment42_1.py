import math

def CalculateEuclideanDistance(p1, p2):
    return math.sqrt(((p1["X"]-p2["X"])**2) + ((p1["Y"]-p2["Y"])**2))

def KNNClassifierX(NewPoint, k = 3):
    border = "-"*30

    Data = [
        {"point" : "A", "X" : 1, "Y" : 2, "label" : "Red"},
        {"point" : "B", "X" : 2, "Y" : 3, "label" : "Red"},
        {"point" : "C", "X" : 3, "Y" : 1, "label" : "Blue"},
        {"point" : "D", "X" : 6, "Y" : 5, "label" : "Blue"}
    ]

    print(border)
    print("KNN Classifier X")
    print(border)

    for i in Data:
        i["distance"] = CalculateEuclideanDistance(i,NewPoint)

    sorted_data = sorted(Data, key=lambda item : item["distance"])

    nearest = sorted_data[:k]
    print(f"Nearest {k} members:")
    for i in nearest:
        print(i) 
    print(border)

    #Voting
    votes = {}
    for neighbor in nearest:
        label = neighbor["label"]
        votes[label] = votes.get(label,0) + 1

    print("Voting result:")
    for d in votes:
        print("Name:",d," Votes:",votes[d])
    print(border)
    
    iMax = 0
    Name = ""
    for i in votes:
        if (votes[i]>iMax):
            iMax = votes[i]
            Name = i

    print("Prediction:",Name)


def main():
    X = int(input("Enter X co-ordinate:"))
    Y = int(input("Enter Y co-ordinate:"))
    KNNClassifierX({"X":X,"Y":Y}, 3)

if (__name__=="__main__"):
    main()