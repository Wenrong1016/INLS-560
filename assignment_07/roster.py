import pandas as pd
def main():
    roster = ["Claude","Brown","Cadeau","Davis","Tyson","Davis","Trimble","Powell","Jackson","Washington"]
    #print(len(roster))
    for i in roster:
        print(i)

    data = pd.DataFrame({"Last Name": roster})
    print(data)
    #data.rename(columns={"0": "Last Name"})
main()