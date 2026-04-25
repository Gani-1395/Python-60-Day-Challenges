Multi-Level Data Replication & Integrity Analyzer
📌 Introduction
The Multi-Level Data Replication & Integrity Analyzer is a Python-based project that simulates how cloud systems replicate user data across multiple servers. In real-world systems, incorrect copying methods may lead to hidden data inconsistency or corruption.
This project demonstrates the difference between assignment copy, shallow copy, and deep copy, while analyzing how modifications in copied data can affect the original data.
🎯 Objective
To understand Python data replication techniques.
To compare assignment, shallow copy, and deep copy.
To detect unexpected changes in original data.
To perform integrity analysis using nested data structures.
To improve problem-solving skills using Python concepts.
🛠️ Technologies Used
Python 3.x
📂 Data Structure Used
The program uses a nested structure:

users = [
    {
        "id": 1,
        "data": {"files": ["a.txt", "b.txt"], "usage": 500}
    },
    {
        "id": 2,
        "data": {"files": ["c.txt"], "usage": 300}
    }
]
This includes:
List
Dictionary
Nested Lists inside Dictionary
⚙️ Functionalities
1️⃣ Data Generation
Creates the original nested user data.
2️⃣ Data Replication
Implements:
Assignment Copy
Shallow Copy
Deep Copy
3️⃣ Data Modification
Performs multi-level modifications such as:
Adding a file
Deleting a file
Updating storage usage
4️⃣ Integrity Analysis
Checks:
Data Leakage
Safe Replication
Common Files Overlap
Mutation Depth
🔐 Personalization Applied
Password-based personalization logic:

a = input("enter the Password: ")

if len(a) == 6 and a == "ganesh":
Rule:
Valid Password → Add new file
Invalid Password → Delete file
This custom rule controls data mutation behavior.
📊 Expected Output
Original Data
Modified Shallow Copy
Safe Deep Copy
Integrity Report
Tuple Output:
Python
(leakage_count, safe_count, overlap_count)
📘 Key Concepts Learned
Difference between shallow copy and deep copy
Behavior of nested mutable objects
Data corruption detection logic
Use of sets, dictionaries, loops, and functions
Real-world cloud replication simulation
🚀 How to Run
Install Python 3.x
Download the project file
Run:
Python
python filename.py
Enter password when prompted.
👨‍💻 Author
Ganesh
