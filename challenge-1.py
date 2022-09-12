x = 1000
sum = 0
while x > 1:
    x = x-1
    if x%3==0 or x%5==0:
        sum = sum + x
print(sum)