n=int(input("enter no of otp:"))
otp=[""]*n
valid=True
for i in range(n):
    otp[i]=input("enter the otp:")
for c in otp:
    for i in range(len(c)):
        for j in range(i+1,len(c)):
            if c[i]==c[j]:
                valid=False
    if (len(c)==6 and c.isdigit()and valid):
       print("Valid OTP")
    else:

      print("Invalid OTP")
