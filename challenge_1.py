name = str(input("Enter your name:"))
email =str(input("Enter your email:"))
number = str(input("Enter your mobile number:"))
age = int(input("Enter your age:"))

if name[0] != " " and name[len(name)-1] != " " and " " in name:
    if email[0] != "@" and email.count("@") == 1 and "." in email:
        if number[0] != "0" and len(number) == 10 and number.isdigit():
            if 18 <= age <= 60:
                print("User Profile is VALID")
            else:
                print("User Profile is INVALID")
        else:
            print("User Profile is INVALID")
    else:
        print("User Profile is INVALID")
else:
    print("User Profile is INVALID")
