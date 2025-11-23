import hcFunction

feet_inches = input("Enter feet and inches: ")
parsed = hcFunction.parse(feet_inches)
result = hcFunction.convert(parsed[0], parsed[1])
print(f"{parsed[0]} feet and {parsed[1]} inches is equal to {result}")

if result < 1:
    print("Kid is too small!")
else:
    print("You can go on the slide")