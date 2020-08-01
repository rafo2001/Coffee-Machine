guests = []
while True:
    guest = input()
    if guest != ".":
        guests.append(guest)
    else:
        break
print(guests)
print(len(guests))