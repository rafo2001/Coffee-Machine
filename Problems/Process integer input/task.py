numbers = []
while True:
    number = int(input())
    if number < 10:
        continue
    elif number > 100:
        break
    else:
        numbers.append(number)
for i in numbers:
    print(i)
