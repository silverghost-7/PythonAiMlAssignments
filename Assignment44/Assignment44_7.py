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
    df["Name"] = df["Name"].replace("Pooja","Puja")
    df["Total"] = df["Math"] + df["Science"] + df["English"]
    plt.bar(df["Name"],df["Total"])
    plt.xlabel("Student name")
    plt.ylabel("Total marks")
    plt.show()

if (__name__=="__main__"):
    main()