v = 0
c = 0

s = input("Enter a string wiithout any space: ")
for i in s:
    if i in "aeiouAEIOU":
        v = v + 1
    else:
        c = c + 1
print("The number of vowels is: ", v)
print("The number of consonants is: ", c)