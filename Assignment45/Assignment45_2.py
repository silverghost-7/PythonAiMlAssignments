import pandas as pd

def main():
    data = {
        "Name" : ["Amit","Sagar","Pooja"],
        "Math" : [85,90,78],
        "Science" : [92,88,80],
        "English" : [75,85,82]
    }

    df = pd.DataFrame(data)
    df["Gender"] = ["F","M","M"]
    df = pd.get_dummies(df,columns=["Gender"])
    print(df)

if (__name__=="__main__"):
    main()