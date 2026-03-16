# Smart Campus Energy Analyzer – README

## 1. Problem Understanding

The objective of this program is to analyze energy consumption readings from multiple buildings and evaluate overall energy efficiency. Each reading is classified into categories such as efficient, moderate, high consumption, or invalid based on predefined ranges. After classification, the program calculates the total energy consumption and number of buildings. Finally, it generates an efficiency report indicating whether the campus has balanced usage, energy waste, or overconsumption.

---

## 2. Logic / Approach Used

The program first asks the user to enter a password and validates that it is exactly 6 characters long and matches the predefined password. After successful authentication, the user enters the number of energy readings and then inputs the readings one by one. A list is used to store the readings, and a **for loop with conditional statements** is used to classify each reading into efficient, moderate, high, or invalid categories, which are stored in a **dictionary**. A **list comprehension** is used to extract valid readings and calculate total energy consumption. Based on certain conditions (high consumption count, total energy usage, and balance between efficient and moderate readings), the program determines the final efficiency result and prints a detailed report.

---

## 3. Personalization Applied

* Personalization Rule: Password must be exactly **6 characters long**.
* The program checks both the **length of the password** and the **exact value ("ganesh")** before allowing access to the energy analysis system.
* This rule was applied to simulate a **basic authentication mechanism**, ensuring that only authorized users can run the program.

---

## 4. Test Case Verification

| Test Case   | Input Readings          | Expected Result          | Output                   |
| ----------- | ----------------------- | ------------------------ | ------------------------ |
| Test Case 1 | 10, 30, 45, 60, 80      | Efficient Campus         | Efficient Campus         |
| Test Case 2 | 120, 150, 200, 180, 100 | Energy Waste Detected    | Energy Waste Detected    |
| Test Case 3 | 200, 190, 170, 160, 150 | Overconsumption Detected | Overconsumption Detected |

---

## 5. Program Features

* Password authentication (6-character validation)
* Input handling using lists
* Data classification using dictionaries
* Use of **loops and conditional statements**
* **List comprehension** for filtering valid readings
* Energy efficiency report generation

---

## 6. Learning Outcome

Through this challenge, I learned how to combine multiple Python concepts such as **lists, dictionaries, loops, conditions, and list comprehensions** to solve a practical data analysis problem. I also understood how to structure logic for classification and decision-making in a program. This exercise improved my ability to organize code and generate meaningful output from user-provided data.
