import pandas as pd

def main():
    data = {
        "Name" : ["Amit","Sagar","Pooja"],
        "Math" : [85,90,78],
        "Science" : [92,88,80],
        "English" : [75,85,82]
    }

    df = pd.DataFrame(data)
    df["Name"] = df["Name"].replace("Pooja","Puja")
    df["Total"] = df["Math"] + df["Science"] + df["English"]
    dfSorted = df.sort_values(by="Total",ascending=False)
    print(dfSorted)

if (__name__=="__main__"):
    main()