import pandas as pd

def LoadDataFromCsv(DataPath):
    DataSet = pd.read_csv(DataPath)
    return DataSet

def main():
    DataPath = "student_performance_ml.csv"
    DataFrame = LoadDataFromCsv(DataPath)
    print("First 5 records:")
    print(DataFrame.head(5))

    print("Last 5 records:")
    print(DataFrame.tail(5))

    print("Total rows:",DataFrame.shape[0])
    print("Total columns:",DataFrame.shape[1])

    print("Column names and types:")
    for col in DataFrame.columns:
        print(f"Name:{col} Type:{type(col)}")

if (__name__=="__main__"):
    main()