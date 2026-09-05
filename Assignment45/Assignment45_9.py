import pandas as pd
import matplotlib.pyplot as plt
def main():
    data = {
        "Name" : ["Amit","Sagar","Pooja"],
        "Math" : [85,90,78],
        "Science" : [92,88,80],
        "English" : [75,85,82]
    }

    df = pd.DataFrame(data)
    labels = ["Math","Science","English"]
    df.rename(columns={"Math":"Mathematics"},inplace=True)
    print(df)

if (__name__=="__main__"):
    main()