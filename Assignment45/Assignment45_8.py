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
    plt.hist(df["Math"],bins=5,edgecolor="black")
    plt.title("Distribution of Math marks")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

if (__name__=="__main__"):
    main()