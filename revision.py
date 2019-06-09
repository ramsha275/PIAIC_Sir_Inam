days = ["Monday" , "Tuesday","Wednedsday","Thursday","Friday", "Saturday","Sunday"]
for day in days:
    if day == "Sunday":
        print("It's holiday")
    else:
        print("You have to go to work")
element = days[2:4]
print(element)
a = days.pop(3)
print(a)
