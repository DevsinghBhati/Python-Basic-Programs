password = input("Enter Password:");

capital = 0
small = 0
length = 0
special_char = ['@' , '#' , '$' , '&']
special_char_count = 0
for i in password:
    if i == i.upper():
        capital += 1
    if i == i.lower():
        small += 1
    if i in special_char:
        special_char_count += 1
    length += 1

if (capital >= 1 and small >= 1 and special_char_count == 1 and length >= 8 ):
    print("Password is strong")
elif(capital < 1):
    print("No capital word")
elif(small <1 ):
    print("No small word")
elif(length < 8):
    print("Password length must be 8")
elif( ' ' in password ):
    print("Password cannot have space")
elif (special_char_count != 1 ) :
    print("Special charcters should  be only one")
