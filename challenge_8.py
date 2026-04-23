import random
import pandas as pd
import numpy as np
import math

a = input("enter the Password: ")
if len(a) == 6 and a == "ganesh":
    print("Valid password")
else:
    print("Invalid password")
    exit()
def generate_data(n):
    data = []
    for i in range(1, n + 1):
        zone = {
            "zone": i,
            "traffic": random.randint(0, 100),
            "air_quality": random.randint(0, 300),
            "energy": random.randint(0, 500)
        }
        data.append(zone)
    data[0]["air_quality"] = 300
    data[1]["traffic"] = 0
    data[2]["traffic"] = 95
    data[2]["energy"] = 470
    return data
def classify_zone(x):
    if x["air_quality"] > 200 or x["traffic"] > 80:
        return "High Risk"
    elif x["energy"] > 400:
        return "Energy Critical"
    elif x["traffic"] < 30 and x["air_quality"] < 100:
        return "Safe Zone"
    else:
        return "Normal"
def calculate_risk(x):
    score = (x["traffic"] * 0.4) + (x["air_quality"] * 0.4) + (x["energy"] * 0.2)
    return round(score, 2)
def sort_by_traffic(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j]["traffic"] > data[j + 1]["traffic"]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data
def final_status(avg):
    if avg < 100:
        return "City Stable"
    elif avg < 170:
        return "Moderate Risk"
    elif avg < 230:
        return "High Alert"
    else:
        return "Critical Emergency"
roll_no = 17
zones = random.randint(15, 20)
city = generate_data(zones)
if roll_no % 3 == 0:
    random.shuffle(city)
else:
    city = sort_by_traffic(city)
category = {}
for i in city:
    i["status"] = classify_zone(i)
    i["risk_score"] = calculate_risk(i)
    i["sqrt_risk"] = round(math.sqrt(i["risk_score"]), 2)
    category[i["zone"]] = i["status"]
df = pd.DataFrame(city)
arr = df[["traffic", "air_quality", "energy"]].values
mean_values = np.mean(arr, axis=0)
risk_list = city[:]
for i in range(len(risk_list)):
    for j in range(0, len(risk_list) - i - 1):
        if risk_list[j]["risk_score"] < risk_list[j + 1]["risk_score"]:
            risk_list[j], risk_list[j + 1] = risk_list[j + 1], risk_list[j]
top3 = risk_list[:3]
risk_tuple = (
    max(df["risk_score"]),
    round(np.mean(df["risk_score"]), 2),
    min(df["risk_score"])
)
threshold = 180
multi_risk = []
for i in range(1, len(city)):
    if city[i]["risk_score"] > threshold and city[i]["air_quality"] > city[i - 1]["air_quality"]:
        multi_risk.append(city[i]["zone"])
traffic_variance = np.var(df["traffic"])
clusters = []
for i in range(len(city) - 1):
    if city[i]["risk_score"] > threshold and city[i + 1]["risk_score"] > threshold:
        clusters.append((city[i]["zone"], city[i + 1]["zone"]))
decision = final_status(risk_tuple[1])
insight = "A smart city controls traffic, reduces pollution, and uses energy efficiently."
print("\nSMART CITY DATA")
print(df)

print("\nZONE CATEGORY")
print(category)

print("\nAVERAGE VALUES")
print("Traffic Mean =", mean_values[0])
print("AQI Mean =", mean_values[1])
print("Energy Mean =", mean_values[2])

print("\nTOP 3 WORST ZONES")
for x in top3:
    print("Zone", x["zone"], "Risk Score =", x["risk_score"])

print("\nRISK SUMMARY")
print(risk_tuple)

print("\nMULTI FACTOR RISK ZONES")
print(multi_risk)

print("\nTRAFFIC VARIANCE")
print(round(traffic_variance, 2))

print("\nCRITICAL CLUSTERS")
print(clusters)

print("\nFINAL DECISION")
print(decision)

print("\nSMART CITY DEFINITION")
print(insight)