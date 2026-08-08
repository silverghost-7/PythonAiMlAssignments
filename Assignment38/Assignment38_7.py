import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def LoadDataFromCsv(DataPath):
    DataSet = pd.read_csv(DataPath)
    return DataSet

def main():
    DataPath = "student_performance_ml.csv"
    DataFrame = LoadDataFromCsv(DataPath)

    plt.figure(figsize=(7,5))
    
    plt.scatter(DataFrame["StudyHours"], DataFrame["PreviousScore"])
    plt.title("Iris Case Study")
    plt.xlabel("StudyHours")
    plt.ylabel("PreviousScore")
    plt.legend()
    plt.grid()
    plt.show()

if (__name__=="__main__"):
    main()