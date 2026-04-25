import copy

def generate_data():
    users = [
        {
            "id": 1,
            "data":{"files": ["a.txt", "b.txt"],"usage": 500}
        },
        {
            "id": 2,
            "data": {"files": ["c.txt"],  "usage": 300}
        }
    ]
    return users

def replicate_data(original):
    assigned = original
    shallow = copy.copy(original)
    deep = copy.deepcopy(original)
    return assigned, shallow, deep

def modify_data(data,roll_number):
   for user in data:

       user["data"]["usage"] +=100

       if roll_number % 2 ==0:
           user["data"]["files"].append("new_file.txt")
       else:
           if user["data"]["files"]:
               user["data"]["files"].pop()

def check_integrity(original,deep):
    leakage_count=0
    safe_count=0
    overlap_count=0

    for i in range(len(original)):
         orig_files = set(original[i]["data"]["files"])
         deep_files = set(deep[i]["data"]["files"])

         if "new_file.txt" in orig_files:
          leakage_count  +=1

         if "new_file.txt" in deep_files:
          safe_count  +=1

         overlap = orig_files.intersection(deep_files)
         overlap_count += len(overlap)

    return leakage_count,safe_count,overlap_count

def main():
    roll_number = 24110011662
    original = generate_data()

    print("\n----BEFORE MODIFICATION----")
    print("original : ", original)
    assigned, shallow, deep = replicate_data(original)

    modify_data(shallow,roll_number)
    modify_data(deep,roll_number)
    print("\n----AFTER MODIFICATION----")
    print("original : ", original)
    print("shallow copy : ", shallow)
    print("deep Copy: ", deep)

    report = check_integrity(original, deep)
    print("\n----INTEGRITY REPORT----")
    print("(leakage_count, safe_count,overlap_count) : ", report)

main()



