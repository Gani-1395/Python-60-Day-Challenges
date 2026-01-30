stu_id=input("ID: ")
mail_id=input("Email: ")
word=input("Password: ")
ref=input("Referral: ")
c=len(mail_id)
if len(stu_id)==7 and stu_id[:3]=="CSE" and stu_id[3]=="-" and stu_id[4:].isdigit():
    if mail_id[0]!= "@" and mail_id[c - 1]!= "@" and mail_id.count("@")==1 and mail_id.count(".")==1 and mail_id[c - 4:]== ".edu":
        if  (len(word)>=8 and "A"<=word[0]<="Z" and
                (word.count("1") or word.count("2") or
                 word.count("3") or word.count("4") or
                 word.count("5") or word.count("6") or
                 word.count("7") or word.count("8") or
                 word.count("9"))):
          if ref[:3]=="REF" and ref[3:5].isdigit() and ref[len(ref)-1:]=="@":
              print("APPROVED")
          else:
              print("REJECTED")
        else:
              print("REJECTED")
    else:
        print("REJECTED")
else:
    print("REJECTED")
