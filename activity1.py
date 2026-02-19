n = int(input("Enter a number of whose sum you want to find: "))
sum = 0 
for i in range(1, n+1):
    sum = sum + i
    print("\n sum =", sum)