import random
import math
import pandas as pd
import numpy as np
import copy

def generate_data(n=15):
    data = []
    for i in range(n):
        zone_data = {
            "zone" : i + 1,
            "metrics" : {
                "traffic" : random.randint(50,200),
                "pollution" : random.randint(30,150),
                "energy" : random.randint(40,180)
            },
            "history" : [random.randint(10,100) for _ in range(5)]
        }
        data.append(zone_data)
    return data

def personalize_data(data,roll_number):
    if roll_number % 2 == 0:
        print("\nRoll Number : ", roll_number, "-> EVEN(divisible by 2)")
        print("Applying PERSONALIZATION: REVERSE DATASET\n")
        return data[::-1]
    else:
        print("\nRoll Number : ", roll_number, "-> ODD(not divisible by 2)")
        print("Applying PERSONALIZATION: ROTATE BY 3\n")
        return data[3:] + data[:3]

def custom_risk_score(traffic,pollution,energy):
    return math.log(traffic + pollution + energy)


def to_dataframe(data):
    rows = []
    for d in data:
        rows.append([
            d["zone"],
            d["metrics"]["traffic"],
            d["metrics"]["pollution"],
            d["metrics"]["energy"]
        ])
    df = pd.DataFrame(rows, columns=["zone","traffic","pollution","energy"])
    return df

def manual_correlation(x,y):
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    num = np.sum((x-mean_x)*(y-mean_y))
    den = math.sqrt(np.sum((x - mean_x) ** 2) * np.sum((y - mean_y) ** 2))

    return num/den if den!=0 else 0

def mutate_data(data):
    for d in data:
        d["metrics"]["traffic"] += random.randint(1,20)
        d["history"].append(random.randint(10,100))
        t= d["metrics"]["traffic"]
        p= d["metrics"]["pollution"]
        e= d["metrics"]["energy"]

        d["risk"] = custom_risk_score(t,p,e)

def detect_anomalies(df):
    anomalies = []
    for col in ["traffic","pollution","energy"]:
        mean = np.mean(df[col])
        std = np.std(df[col])

        for i,val in enumerate(df[col]):
            if val > mean+std:
                anomalies.append((df["zone"][i],col,val))
    return anomalies

def stability_index(df):
    variance = np.var(df[["traffic","pollution","energy"]].values)
    return 1 / variance if variance !=0 else 0

def detect_clusters(data,threshold=5):
    clusters = []
    current_cluster = []

    for d in data:
        if d.get("risk",0) > threshold:
            current_cluster.append(d["zone"])
        else:
            if len(current_cluster)>1:
                clusters.append(current_cluster)
            current_cluster = []
    if len(current_cluster)>1:
        clusters.append(current_cluster)

    return clusters

roll_number = 24110011662

original_data = generate_data()

original_data = personalize_data(original_data,roll_number)

assigned_copy = original_data
shallow_copy = copy.copy(original_data)
deep_copy = copy.deepcopy(original_data)

print("------BEFORE MUTATION------")
print("Original Traffic :", original_data[0]["metrics"]["traffic"])

mutate_data(shallow_copy)
mutate_data(deep_copy)

print("\n -----AFTER MUTATION-------")
print("Original Traffic: " , original_data[0]["metrics"]["traffic"])
print("Shallow Traffic: " , shallow_copy[0]["metrics"]["traffic"])
print("Deep Traffic: " , deep_copy[0]["metrics"]["traffic"])

df = to_dataframe(original_data)

mean_vals = df.mean()
variance_vals = df.var()
corr_tp = manual_correlation(df["traffic"].values,df["pollution"].values)

anomalies = detect_anomalies(df)
stability = stability_index(df)

risks = [d.get("risk",0) for d in original_data]
max_risk = max(risks)
min_risk = min(risks)

clusters = detect_clusters(original_data)

if max_risk > 6:
    decision = "Critical Failure"
elif max_risk >5:
    decision = "High Corruption Risk"
elif max_risk >4:
    decision = "Moderate Risk"
else:
    decision = "System Stable"

print("\n=====DATAFRAME======")
print(df)

print("\n======ANALYSIS======")
print("Mean: \n", mean_vals)
print("Variance: \n", variance_vals)
print("Manual Correlation (Traffic vs Pollution): ", corr_tp)

print("\n=====ANOMALIES======")
for a in anomalies:
    print(a)

print("\n====CLUSTERS======")
print(clusters)

print("\n====FINAL METRICS=======")
print("Tuple (max_risk,min_risk,stability):", (max_risk,min_risk,stability))

print("\n=====FINAL DECISION======")
print(decision)




