for i in range(10, 100):     
    if (i//10 + i%10)**2 == i:
            print(i)
for i in range(1, 100):
    divisor_count = 0
    for j in range(1, i+1):
        if i%j == 0:
            divisor_count += 1
    if divisor_count == 10:
        print(i)