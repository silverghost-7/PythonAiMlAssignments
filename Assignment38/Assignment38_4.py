import pandas as pd

def LoadDataFromCsv(DataPath):
    DataSet = pd.read_csv(DataPath)
    return DataSet

def main():
    DataPath = "student_performance_ml.csv"
    DataFrame = LoadDataFromCsv(DataPath)

    print("Class distribution (FinalResult): ")
    print(DataFrame["FinalResult"].value_counts())

    cntPassed = len(list(filter(lambda val : val==1, DataFrame["FinalResult"])))
    cntFailed = len(list(filter(lambda val : val!=1, DataFrame["FinalResult"])))
    print("Pass percentage:",cntPassed/DataFrame.shape[0]*100)
    print("Fail percentage:",cntFailed/DataFrame.shape[0]*100)

if (__name__=="__main__"):
    main()