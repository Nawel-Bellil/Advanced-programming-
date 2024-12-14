name1 = input("Runner 1:\nName: ")
t1 = float(input("Time (in seconds): "))
name2 = input("Runner 2:\nName: ")
t2 = float(input("Time (in seconds): "))

if t1 < t2:
    print(f"The faster runner is {name1}")
elif t2 < t1:
    print(f"The faster runner is {name2}")
else:
    print(f"{name1} and {name2} have the same time")
