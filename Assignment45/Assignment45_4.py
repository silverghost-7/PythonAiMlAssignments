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
    marks = df[df["Name"]=="Sagar"][["Math","Science","English"]].values.flatten()
    plt.pie(marks,labels=labels,autopct="%1.1f%%")
    plt.title("Sagar's subject viz distribution")
    plt.show()

if (__name__=="__main__"):
    main()