# Data Splitter and Conditional Reversal Program
## Overview
This Python program takes mixed user input (numbers and strings), separates them into two lists, and conditionally reverses one of the lists based on the last digit of a registration number.
It demonstrates:

- Input handling
- String and numeric validation
- List manipulation
- Conditional logic
- Counting elements

---

## Features

- Accepts multiple user inputs
- Separates numeric and string values
- Counts numbers and strings
- Reverses a list depending on registration number parity
- Displays final results clearly

---

## How It Works

1. User enters how many values they want to input.
2. Program stores all inputs.
3. Each value is checked:
   - Numbers → stored in `num_lst`
   - Strings → stored in `str_lst`
4. User enters a registration number.
5. If the last digit is:
   - **Even** → reverse number list
   - **Odd** → reverse string list
6. Program prints final lists and counts.

---

## Code

```python
m=int(input())
data=[0]*m
num_lst=[""]*m
str_lst=[" "]*m
n_count=0
s_count=0
for i in range(m):
    data[i]=(input())
for i in range(m):
    if data[i].isdigit():
        num_lst[n_count] = int(data[i])
        n_count += 1
    elif data[i] != '""':
        str_lst[s_count] = data[i]
        s_count += 1
num_lst = num_lst[:n_count]
str_lst = str_lst[:s_count]
reg_no = input("enter the registration number:")
if int(reg_no[-1]) % 2 == 0:
    num_lst = num_lst[::-1]
else:
    str_lst = str_lst[::-1]
print("Numbers List:", num_lst)
print("String List:", str_lst)
print("Total Numbers:", n_count)
print("Total Strings:", s_count)
```

---

## Example Run

```
Input:
5
10
hello
25
world
99
Registration: 1234

Output:
Numbers List: [99, 25, 10]
String List: ['hello', 'world']
Total Numbers: 3
Total Strings: 2
```

---

## Requirements

- Python 3.x

---

## How to Run

```bash
python filename.py
```

---

## Author

Ganesh

---

## License
This project is open-source and free to use.
