age = int(input("Enter your age: "))

if age < 0:
    print("Age could not be less than 0")
elif age < 18:
    print("You are less than 18")
else:
    print("You are above 18")
    