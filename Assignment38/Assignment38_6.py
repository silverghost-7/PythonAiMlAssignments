import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def LoadDataFromCsv(DataPath):
    DataSet = pd.read_csv(DataPath)
    return DataSet

def main():
    DataPath = "student_performance_ml.csv"
    DataFrame = LoadDataFromCsv(DataPath)

    plt.hist(DataFrame["StudyHours"])
    plt.show()

if (__name__=="__main__"):
    main()