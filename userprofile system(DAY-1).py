name= input("Enter your name: ")
email= input("Enter your email: ")
mobile_no= input("Enter your mobile number: ")
age= int(input("Enter your age: "))
valid = True

if name.count(" ") >=1 and   name[0] != " "  and name[-1] != " " :
       pass
else :
       valid = False

if "@" in email and "." in email and email[0] != "@"  :
      pass
else :
    valid = False


if len(mobile_no)==10 and mobile_no.isdigit() and mobile_no[0] !=0 :
         pass
else:
    valid = False

if age >=18 and age <=60 :
      pass
else:
    valid = False

if valid :
    print("USER PROFILE IS VALID")
else  :
    print("USER PROFILE IS INVALID")