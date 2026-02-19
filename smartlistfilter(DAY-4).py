data = [10,"python","",25,"loop",40]
number_list=[]
string_list=[]
num_count=0
str_count=0
for i in data:
      if type(i)==int :
          num_count+=1
          number_list.append(i)
      elif type(i)==str and i !="" :
          str_count+=1
          string_list.append(i)

print( " initial number list :",number_list)
print( " initial string list :",string_list)
print( " number count in number list :",num_count)
print( " string count  in string list :",str_count)


name = "Mounish"
if len(name)%2!=0 :
         del number_list[len(number_list)-1]
         del string_list[len(string_list)-1]
else :
         del number_list[0]
         del string_list[0]

print("the updated number list after personalization :",number_list)
print("the updated string list after personalization :",string_list)











