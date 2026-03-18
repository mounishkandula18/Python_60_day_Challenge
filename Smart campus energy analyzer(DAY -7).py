energies = [23,-7,45,67,109,189,324]
data = {
    "invalid" : [],
    "efficient" : [],
    "moderate" : [],
    "high" : []
}
for e in energies:
    if e < 0:
        data["invalid"].append(e)
    elif e<=50:
        data["efficient"].append(e)
    elif e<=150:
        data["moderate"].append(e)
    else:
        data["high"].append(e)

    total_consumption =sum([e for e in energies if e >= 0])

    summary = (
        len(data["invalid"]),
        len(data["efficient"]),
        len(data["moderate"]),
        len(data["high"]),
    )
if len(data["high"]) > 3:
    result = "high"
elif abs(len(data["efficient"]) - len(data["moderate"])) <=1:
    result = "Balanced Usage"
elif total_consumption > 600:
    result = "Energy waste Detected"
else :
    result = "Moderate Usage"

print("\n---Energy Efficiency Report---")
print("Efficient :",data["efficient"])
print("Moderate :",data["moderate"])
print("High :",data["high"])
print("Invalid:",data["invalid"])

print("\nTotal Consumption :",total_consumption)
print("Number of buildings",len(energies))
print("Summary info(Eff,Mod,High,Invalid):",summary)
print("Final result:",result)

name = "Mounish"
if len(name)%2 !=0:
    total_consumption *=0.9
else:
    total_consumption *=1.1
print("Total Consumption after applied  personalization logic :",total_consumption)







