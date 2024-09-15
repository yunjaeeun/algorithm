while True:
    name, age, weight = input().split()
    age = int(age)
    weight = int(weight)
    if age >= 18 or weight >= 80:
        print(name, "Senior")
    elif name == "#":
        break
    else:
        print(name, "Junior")
