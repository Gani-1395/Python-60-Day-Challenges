# Autonomous Smart City Data Intelligence System

## 📌 Project Description
The **Autonomous Smart City Data Intelligence System** is a Python-based project designed to simulate and analyze smart city sensor data. It collects and processes data such as **traffic density**, **air quality index (AQI)**, and **energy consumption** from multiple city zones.  

The main objective of this project is to identify risky zones, detect unusual patterns, and predict the overall condition of the city using Python and Data Science tools.

---

## 🚀 Features
- Simulates data for **15 to 20 city zones**
- Stores records using **list of dictionaries**
- Converts data into a **Pandas DataFrame**
- Uses **NumPy** for numerical analysis
- Uses **math module** for square root transformation
- Calculates a **custom risk score**
- Classifies zones into:
  - High Risk
  - Energy Critical
  - Safe Zone
  - Normal
- Finds the **Top 3 highest risk zones**
- Detects:
  - Multi-factor risk patterns
  - Traffic stability using variance
  - Consecutive critical clusters
- Displays final smart city status

---

## 🛠️ Technologies Used
- Python  
- Pandas  
- NumPy  
- Random Module  
- Math Module  

---

## 📊 Input Parameters
Each zone contains:

- **Zone ID**
- **Traffic Density** (0–100)
- **Air Quality Index** (0–300)
- **Energy Consumption** (0–500)

---

## 📈 Risk Score Formula
A customized formula is used:

risk_score = (traffic × 0.4) + (air_quality × 0.4) + (energy × 0.2)

This formula gives more importance to traffic and pollution levels.

---

## 🔐 Personalization Added
This project includes a password validation feature:

- User must enter password: **ganesh**
- Password length must be exactly **6 characters**

Only valid users can access the system.

---

## 🧠 Final Decision Levels
Based on average risk score:

- **City Stable**
- **Moderate Risk**
- **High Alert**
- **Critical Emergency**

---

## 🎯 Learning Outcomes
Through this project, I learned:

- How to use Python for real-world problem solving
- Data analysis using Pandas and NumPy
- Working with conditions, loops, and functions
- Risk prediction using custom logic
- Building intelligent smart systems

---

## 👨‍💻 Author
**Ganesh**
