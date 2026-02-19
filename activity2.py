string = input("Enter a string: ")
string_2 = ""

for i in string:
    string_2 = i + string_2
    
print("\nThe original string is: ", string)
    
print("The reverse of the string is: ", string_2)