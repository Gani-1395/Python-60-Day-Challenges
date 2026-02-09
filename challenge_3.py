reg_no=input("enter the registration number:")
if reg_no[:2]=="AP" and len(reg_no)==13 and reg_no[2:].isdigit():
    print("Valid Registration Number")
else:
    print("Invalid Registration Number")
n = int(input())
marks = [0] * n
for i in range(n):
    marks[i]=int(input())
valid=0
failed=0
for mark in marks:
        if 100>=mark>=90:
            print(mark,"->Excellent")
            valid+=1
        elif 89>=mark>=75:
            print(mark, "->Very Good")
            valid += 1
        elif 74>=mark>=60:
            print(mark, "->Good")
            valid += 1
        elif 59>=mark>=40:
            print(mark, "->Average")
            valid += 1
        elif 39>=mark>=0:
            print(mark, "->Fail")
            valid += 1
            failed += 1
        else:
            print(mark, "->Invalid")
print("Total Valid Students:",valid)
print("Total Failed Students:",failed)