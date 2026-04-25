import random
import math
import copy
import numpy as np
import pandas as pd

def password_check():
    a = input("enter the Password: ")
    if len(a) == 6 and a == "ganesh":
        print("Valid password")
        return a
    else:
        print("Invalid password")
        return None

def generate_data(n):
    data = []
    for i in range(1, n + 1):
        data.append({
            "zone": i,
            "metrics": {
                "traffic": random.randint(50, 200),
                "pollution": random.randint(20, 150),
                "energy": random.randint(30, 180)
            },
            "history": [random.randint(40, 150) for _ in range(5)]
        })
    return data

def personalize_data(data, a):
    if len(a) == 6 and a == "ganesh":
        data.reverse()
    else:
        data = data[3:] + data[:3]
    return data

def custom_risk_score(t, p, e):
    return math.log(t + p + e) + math.sqrt((t * p) / (e + 1))

def convert_dataframe(data):
    rows = []
    for item in data:
        rows.append([
            item["zone"],
            item["metrics"]["traffic"],
            item["metrics"]["pollution"],
            item["metrics"]["energy"],
            sum(item["history"]) / len(item["history"])
        ])
    return pd.DataFrame(rows, columns=["Zone", "Traffic", "Pollution", "Energy", "HistoryAvg"])

def manual_corr(x, y):
    xm = np.mean(x)
    ym = np.mean(y)
    num = np.sum((x - xm) * (y - ym))
    den = math.sqrt(np.sum((x - xm) ** 2) * np.sum((y - ym) ** 2))
    return num / den

def detect_clusters(risky):
    clusters = []
    temp = []
    for i in risky:
        if not temp:
            temp.append(i)
        elif i == temp[-1] + 1:
            temp.append(i)
        else:
            if len(temp) > 1:
                clusters.append(temp)
            temp = [i]
    if len(temp) > 1:
        clusters.append(temp)
    return clusters

a = password_check()

if a:

    data = generate_data(15)
    data = personalize_data(data, a)

    print("BEFORE COPY")
    for i in data[:2]:
        print(i)

    assign_copy = data
    shallow_copy = copy.copy(data)
    deep_copy = copy.deepcopy(data)

    shallow_copy[0]["metrics"]["traffic"] = 999
    shallow_copy[0]["history"].append(777)

    for item in data:
        m = item["metrics"]
        item["risk"] = custom_risk_score(m["traffic"], m["pollution"], m["energy"])

    df = convert_dataframe(data)

    traffic = df["Traffic"].to_numpy()
    pollution = df["Pollution"].to_numpy()

    mean_val = np.mean(traffic)
    var_val = np.var(traffic)
    std_val = np.std(traffic)

    corr_tp = manual_corr(traffic, pollution)

    anomaly_zones = []
    for i in range(len(traffic)):
        if traffic[i] > mean_val + std_val:
            anomaly_zones.append(int(df["Zone"][i]))

    risky = []
    for item in data:
        if item["risk"] > 20:
            risky.append(item["zone"])

    clusters = detect_clusters(sorted(risky))

    stability_index = 1 / (var_val + 1)

    risk_values = [i["risk"] for i in data]
    result_tuple = (max(risk_values), min(risk_values), stability_index)

    if len(anomaly_zones) == 0 and stability_index > 0.01:
        decision = "System Stable"
    elif len(anomaly_zones) < 3:
        decision = "Moderate Risk"
    elif len(anomaly_zones) < 6:
        decision = "High Corruption Risk"
    else:
        decision = "Critical Failure"

    print("\nAFTER SHALLOW COPY MUTATION")
    print(data[0])

    print("\nDEEP COPY FIRST ZONE")
    print(deep_copy[0])

    print("\nDATAFRAME")
    print(df)

    print("\nMean =", mean_val)
    print("Variance =", var_val)
    print("Correlation =", corr_tp)

    print("\nAnomaly Zones =", anomaly_zones)
    print("Risky Zones =", risky)
    print("Clusters =", clusters)

    print("\nTuple Output =", result_tuple)

    print("\nWhy shallow copy corrupts nested structures?")
    print("Because inner dict and list references are shared with original.")

    print("\nFinal Decision =", decision)