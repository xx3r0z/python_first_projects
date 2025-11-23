password = input("Enter a password: ")
result = {}

if len(password) > 8:
    result["length"] = True
else:
    result["length"] = False

number = False
for i in password:
    if i.isdigit():
        number = True
result["number"] = number

high_letter = False
for i in password:
    if i.isupper():
        high_letter = True
result["high_letter"] = high_letter

# all() returns boolean
if all(result.values()):
    print("Strong Password!")
else:
    print("Weak Password!")

