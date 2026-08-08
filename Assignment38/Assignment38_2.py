import pandas as pd

def LoadDataFromCsv(DataPath):
    DataSet = pd.read_csv(DataPath)
    return DataSet

def main():
    DataPath = "student_performance_ml.csv"
    DataFrame = LoadDataFromCsv(DataPath)

    print("Total number of students:",DataFrame.shape[0])
    cntPassed = len(list(filter(lambda val : val==1, DataFrame["FinalResult"])))
    print("Students passed:",cntPassed)

    cntFailed = len(list(filter(lambda val : val!=1, DataFrame["FinalResult"])))
    print("Students failed:",cntFailed)

if (__name__=="__main__"):
    main()