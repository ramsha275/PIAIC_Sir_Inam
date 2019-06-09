days = ('monday','tuesday','wednesday','thursday','friday','saturday','sunday')
print(days)
print(days[1])
days = list(days)
days[0]='sunday'
days = tuple(days)
print(days)
for day in range(0,len(days)):
    if days[day] == "sunday":
        print("Today is holiday")
    else:
        print("You have to work today ")

