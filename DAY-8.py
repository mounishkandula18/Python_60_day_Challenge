import random
import math
import numpy as np
import pandas as pd

def generate_data(n=18):
    data = []

    for i in range(1, n+1):
       record ={
           "zone" : i,
           "traffic" :random.randint(0,100),
           "air_quality" :random.randint(0,300),
           "energy" :random.randint(0,500),
       }
       data.append(record)

    data.append({"zone" : 99, "traffic" : 0, "air_quality" : 50, "energy" : 100})
    data.append({"zone" : 100, "traffic" : 95, "air_quality" :290, "energy" : 480})

    return data


def classify_zone(record):
    if record["air_quality"] > 200 or record["traffic"] > 80:
        return "High risk"
    elif record["energy"] > 400:
        return "Energy critical"
    elif record["traffic"] <30 and record["air_quality"] < 100:
        return "Safe Zone"
    else:
        return "Moderate"

def calculate_risk_score(df):
    df["risk_score"] = (
         df["traffic"] * 0.4 + df["air_quality"] * 0.4 + df["energy"] * 0.2
    )
    return df

def custom_sort(data,key):
    return sorted(data,key=lambda x:x[key],reverse=True)

def analyze_data(df):
    print("\n---Mean Values----")
    print(df[["traffic","air_quality","energy"]].mean())

    records = df.to_dict("records")
    sorted_records = custom_sort(records,"risk_score")
    top3 = sorted_records[:3]

    print("\n---Top 3 Risk Zones----")
    for r in top3:
        print(r)
    return top3

def detect_pattern(df):


    threshold = df["risk_score"].mean()

    multi_risk = df[df["risk_score"]>threshold]

    traffic_var = np.var(df["traffic"])
    stable = traffic_var < 500

    clusters =[]
    temp=[]
    for i in range(len(df)):
        if df.iloc[i]["risk_score"]>threshold:
            temp.append(int(df.iloc[i]["zone"]))
        else:
            if len(temp)>=2:
                clusters.append(temp)
            temp = []
    return multi_risk, stable, clusters

def system_decision(df):
    avg = df["risk_score"].mean()

    if avg < 100:
        return "city stable"
    elif avg < 200:
        return " moderate risk"
    elif avg < 300:
        return " High Alert"
    else:
        return " Critical Emergency"

def main():
    data = generate_data()

    roll_number = 24110011662
    if  roll_number % 3 == 0:
        random.shuffle(data)
    else:
        data = sorted(data,key=lambda x:x["traffic"])

    for d in data:
        d["category"] = classify_zone(d)

    df = pd.DataFrame(data)

    df = calculate_risk_score(df)

    df["sqrt_risk"] = df["risk_score"].apply(math.sqrt)
    print("\n---DataFrame----")
    print(df)

    analyze_data(df)
    multi_risk, stable ,clusters = detect_pattern(df)

    print("\n---Multi-factor Risk Zones---")

    print(multi_risk[["zone","risk_score"]])
    print("\nStability :", "Stable" if stable else "Not stable")
    print("\nCritical Clusters :", clusters)

    result_tuple = (
              df["risk_score"].max(),
              df["risk_score"].mean(),
              df["risk_score"].min()
)
    print("\n---Risk Tuple----")
    print(result_tuple)

    decision = system_decision(df)
    print("\n---Final Decision----")
    print(decision)

    print("\n---Smart City Insights----")
    print(" A Smart city intelligently balances traffic, pollution , and energy using data-driven decisions.")

main()





