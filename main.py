print("Welcome to receipt calculator!")

receipt = float(input("Please give the amount You paid: "))
tip = int(input("How much tip do you wanna leave? (10, 12 or 15) "))
split = int(input("How many people do You want to include? "))

calculator = receipt * (1 + (tip/100)) / split

final_amount = "{:.2f}".format(calculator, 2)

if tip == 10:
    print(f"Each person should pay: {final_amount} zloty")
elif tip == 12:
    print(f"Each person should pay: {final_amount} zloty")
else:
    print(f"Each person should pay: {final_amount} zloty")

# the end
