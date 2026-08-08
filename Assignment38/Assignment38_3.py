import pandas as pd

def LoadDataFromCsv(DataPath):
    DataSet = pd.read_csv(DataPath)
    return DataSet

def main():
    DataPath = "student_performance_ml.csv"
    DataFrame = LoadDataFromCsv(DataPath)

    studyHours = DataFrame["StudyHours"]
    print("Average study hours:",sum(studyHours)/len(studyHours))

    attendance = DataFrame["Attendance"]
    print("Average attendance:",sum(attendance)/len(attendance))

    maxPreviousScore = max(DataFrame["PreviousScore"])
    print("Maximum PreviousScore:",maxPreviousScore)

    minSleepHours = max(DataFrame["SleepHours"])
    print("Minimum SleepHours:",minSleepHours)

if (__name__=="__main__"):
    main()