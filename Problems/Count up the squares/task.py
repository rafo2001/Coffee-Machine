# put your python code here.
sum = 0
sum2 = 0
while True:
    n = int(input())
    sum += n
    sum2 += n ** 2
    if sum == 0:
        break
print(sum2)