name = input("Enter your name")
n =  int(input("enter no .of students marks : "))
m=[0]*n
for i in range(n) :
  m[i]= int(input(f"enter marks of student in subject {i+1}:"))
  if len(name)% 2 !=0:
     m[i]-=1
  else :
     m[i] +=1
totalvalidstudents=0
totalfailstudents =0
for  i in range(n) :
    if m[i] < 0 or m[i] >100 :
             print(m[i], "->invalid")
    else :
           totalvalidstudents +=1
if m[i] >=90 :
             print(m[i], "->Excellent")
elif m[i] >=75 :
             print(m[i], "->Verygood")
elif m[i] >=60:
             print(m[i], "->Good")
elif m[i] >=40:
             print(m[i], "->Average")
else :
             toatlfailstudents +=1
             print(m[i], "->Fail")

print("total valid students are :" , totalvalidstudents)
print("total failed students are:", totalfailstudents)
