import math

def CalculateEuclideanDistance(p1, p2):
    return math.sqrt(((p1["X"]-p2["X"])**2) + ((p1["Y"]-p2["Y"])**2))

def KNNClassifierX(NewPoint, k = 3):
    Data = [
        {"point" : "A", "X" : 1, "Y" : 2, "label" : "Red"},
        {"point" : "B", "X" : 2, "Y" : 3, "label" : "Red"},
        {"point" : "C", "X" : 3, "Y" : 1, "label" : "Blue"},
        {"point" : "D", "X" : 6, "Y" : 5, "label" : "Blue"}
    ]

    for i in Data:
        i["distance"] = CalculateEuclideanDistance(i,NewPoint)

    sorted_data = sorted(Data, key=lambda item : item["distance"])

    nearest = sorted_data[:k]

    #Voting
    votes = {}
    for neighbor in nearest:
        label = neighbor["label"]
        votes[label] = votes.get(label,0) + 1

    iMax = 0
    Name = ""
    for i in votes:
        if (votes[i]>iMax):
            iMax = votes[i]
            Name = i

    return Name


def main():
    X = int(input("Enter X co-ordinate:"))
    Y = int(input("Enter Y co-ordinate:"))

    for i in range(0,3):
        k = (2*i)+1
        Prediction = KNNClassifierX({"X":X,"Y":Y}, k)
        print(f"K = {k} -> {Prediction}")

if (__name__=="__main__"):
    main()