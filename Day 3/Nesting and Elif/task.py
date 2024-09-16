print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay 100rs.")
    elif age > 12 and age < 18:
        print("Please pay 150rs.")
    elif age >= 18:
        print("Please pay 200rs.")
else:
    print("Sorry you have to grow taller before you can ride.")
