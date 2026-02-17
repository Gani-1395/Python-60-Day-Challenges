# Python Load Classification Challenge

This repository contains a Python program that classifies numeric inputs into different load categories and demonstrates conditional output based on string length logic.

---

## Program Description

The program performs the following:

1. Takes a favorite number input from the user.
2. Validates the input to ensure it is numeric.
3. Takes `m` numeric values from the user.
4. Classifies each value into one of five categories:
   - **Very Light:** 0–5
   - **Normal Load:** 6–25
   - **Heavy Load:** 26–60
   - **Overload:** >60
   - **Invalid Entries:** <0
5. Uses counters to manage list indices (no `append()` used).
6. Checks a string `"ALURU GANESH"`:
   - Removes spaces and calculates `(length % 3)`.
   - If remainder is 2:
     - Prints normal and heavy loads.
   - Otherwise prints `"invalid number"`.

---

##  Input & Output Example

**Sample Run:**

enter your favourite number: 5
Enter value: 3
Enter value: 12
Enter value: 30
Enter value: 65
Enter value: -1
normal: [12]
heavy: [30]


Explanation:

- `3` → Very Light  
- `12` → Normal Load  
- `30` → Heavy Load  
- `65` → Overload  
- `-1` → Invalid Entry  

Conditional output is based on the string `"ALURU GANESH"`.

---
