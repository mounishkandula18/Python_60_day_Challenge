weights = [2,10,35,70,-5,25,5,60,80]
name = "KandulaMounish"
L = len(name)
PLI = L%3
very_light = []
normal_load =[]
heavy_load =[]
overload = []
invalid_entries = []
for w in weights:
    if w <=0 :
        invalid_entries.append(w)
    elif  w<=5 :
        very_light.append(w)
    elif w <=25 :
        normal_load.append(w)
    elif  w <=60 :
        heavy_load.append(w)
    else :
        overload.append(w)



print("Initial list of invalid entries:", invalid_entries)
print("Initial list of very light:", very_light)
print("Initial list of normal load:",normal_load)
print("Initial list of heavy load:", heavy_load)
print("Initial list of overload:", overload)
affected =0
if PLI == 0 :
    for w in overload:
        invalid_entries.append(w)
        affected +=1
        overload = []
elif PLI == 1 :
    affected=len(very_light)
    very_light = []
elif PLI == 2 :
    affected=len(very_light) + len(overload)
    very_light = []
    overload = []
final_plan = []
for w in very_light:
    final_plan.append(w)
for w in normal_load:
    final_plan.append(w)
for w in heavy_load:
    final_plan.append(w)
for w in overload:
    final_plan.append(w)

valid_count = 0
for w in weights:
    if w >=0 :
        valid_count += 1


print("Length(L):",L)
print("PLI value :",PLI)
print("Affected Items:",affected)
print("Total valid Weights :", valid_count)

print("...Final List....")
print("very_light:",very_light)
print("normal_load:",normal_load)
print("heavy_load:",heavy_load)
print("overload:",overload)
print("invalid_entries:",invalid_entries)
print("Final plan :",final_plan)



