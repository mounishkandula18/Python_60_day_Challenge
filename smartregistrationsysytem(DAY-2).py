student_ID = input("Enter student ID : ")
email_ID = input("Enter student email : ")
password = input("Enter password : ")
Referral_code = input("Enter Referral code : ")
valid = True
if  len(student_ID) ==7 and student_ID[0:3] == "CSE"  and student_ID[3] == "-" and student_ID[-3:].isdigit() :
      pass
else:
      valid = False

if "@" in email_ID and "." in email_ID :
     if email_ID[0] !="@" and email_ID[-1] !="@" and email_ID[-4: ] == ".edu" :
         pass
     else :
         valid = False
else :
     valid = False

if len(password)>=8 :
    if 'A' <= password[0] <= 'Z' and any(ch.isdigit() for ch in password) :
         pass
    else :
        valid = False
else:
    valid = False
if len(Referral_code) == 6 and Referral_code[0:3] == "REF" and Referral_code[3 : 5].isdigit()  and Referral_code[-1] == "@" :
    pass
else:
    valid = False

if valid:
    print("APPROVED")
else:
    print("REJECTED")

