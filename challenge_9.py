import copy
users = [
    {
        "id": 1,
        "data": {"files": ["a.txt", "b.txt"], "usage": 500}
    },
    {
        "id": 2,
        "data": {"files": ["c.txt"], "usage": 300}
    }
]
a = input("enter the Password: ")

if len(a) == 6 and a == "ganesh":
    rule = "add"
else:
    rule = "delete"

def generate_data():
    return users
def replicate_data(data):
    assigned = data
    shallow = copy.copy(data)
    deep = copy.deepcopy(data)
    return assigned, shallow, deep
def modify_data(shallow_data):
    if rule == "add":
        shallow_data[0]["data"]["files"].append("new_file.txt")
    else:
        if len(shallow_data[0]["data"]["files"]) > 0:
            shallow_data[0]["data"]["files"].pop()
    shallow_data[0]["data"]["usage"] = 900
    shallow_data[1]["data"]["files"].remove("c.txt")
def check_integrity(original, deep_data):
    leakage = 0
    safe = 0
    if original[0]["data"]["files"] != ["a.txt", "b.txt"]:
        leakage += 1
    if deep_data[0]["data"]["files"] == ["a.txt", "b.txt"]:
        safe += 1
    set1 = set(original[0]["data"]["files"])
    set2 = set(["a.txt", "b.txt"])
    overlap = len(set1.intersection(set2))
    return (leakage, safe, overlap)
original = generate_data()

print("BEFORE MODIFICATION")
print(original)
assigned, shallow, deep = replicate_data(original)
modify_data(shallow)

print("AFTER MODIFICATION")
print("Original Data:", original)
print("Shallow Copy:", shallow)
print("Deep Copy:", deep)

report = check_integrity(original, deep)

print("Integrity Report")
print(report)

print("Inner list got affected because shallow copy shares nested references.")
print("Deep copy remains unchanged because it uses separate memory.")
print("If original data changes after modifying copied data, corruption occurred.")