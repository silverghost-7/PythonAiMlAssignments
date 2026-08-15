import math

StudyHours = "Study Hours"
Attendance = "Attendance"
Result = "Result"

def CalculateEuclideanDistance(p1, p2):
    return math.sqrt(((p1[StudyHours]-p2[StudyHours])**2) + ((p1[Attendance]-p2[Attendance])**2))

def KNNClassifierX(NewPoint, k = 3):
    Data = [
        {StudyHours : 2, Attendance : 60, Result : "Fail"},
        {StudyHours : 5, Attendance : 80, Result : "Pass"},
        {StudyHours : 6, Attendance : 85, Result : "Pass"},
        {StudyHours : 1, Attendance : 50, Result : "Fail"}
    ]

    for i in Data:
        i["distance"] = CalculateEuclideanDistance(i,NewPoint)

    sorted_data = sorted(Data, key=lambda item : item["distance"])

    nearest = sorted_data[:k]

    #Voting
    votes = {}
    for neighbor in nearest:
        label = neighbor[Result]
        votes[label] = votes.get(label,0) + 1

    iMax = 0
    Name = ""
    for i in votes:
        if (votes[i]>iMax):
            iMax = votes[i]
            Name = i

    return Name


def main():
    X = int(input("Enter study hours:"))
    Y = int(input("Enter attendance:"))

    Prediction = KNNClassifierX({StudyHours:X,Attendance:Y})
    print("Predicted Result: ",Prediction)

if (__name__=="__main__"):
    main()