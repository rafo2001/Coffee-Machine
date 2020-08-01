days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
refday = 2
refhour = 10
offset = int(input())
newhour = refhour+offset
if newhour < 0:
    newday = refday - 1
elif newhour >= 24:
    newday = refday + 1
else:
    newday = refday
print(days[newday])
