i = 1
sum = 0
while i < 100:
    if i%2 == 0:
        sum = sum - i
    else:
        sum = sum +  i
    i += 1
print("和是%d"%sum)
