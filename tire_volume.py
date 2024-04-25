
#importing math and datetime moudlues 
import math
from datetime import datetime

# Descrinption of the program to the user
print("This a programm that take inputs from a user")
print("to compute the volume of a tire in litters to")
print("to determine the price of the tire")
print()

# Getting the various input from the user
width=float(input("Enter width of the tire in millimeters(ex 205): "))
aspect_ratio=float(input("Enter asepect_ ratio of the tire (60)  : "))
diameter=float(input("Enter diameter of the while in inches(ex 15)  :"))


# Computing the value for the numerator of the volume function 
volume_numerator= math.pi * (width**2)* aspect_ratio * (width * aspect_ratio + 2540 * diameter)
# Computing the tire volume 
volume= volume_numerator/10000000000
print(f"The approximated volume the tire is {volume:.2f} liters")
#Generating the current date and time
date_and_time=datetime.now().strftime("%Y-%m-%d")

# Appending values to the volume function
with open("volumes.txt","a") as file:
    file.write(f"{date_and_time},{width},{aspect_ratio},{diameter},{volume:.2f}\n")


 #Tire prices based on tire dimensions
if width == 205 and aspect_ratio == 60 and diameter == 15:
    price = 100
elif width == 225 and aspect_ratio == 45 and diameter == 17:
    price = 120
elif width == 195 and aspect_ratio == 55 and diameter == 19:
    price = 90
elif width == 275 and aspect_ratio == 40 and diameter == 20:
    price = 200
else:
    price = None

# Printing the tire price if available or not avalible for the user's dimensions 
if price is not None:
    print(f"The tire price for the specified dimensions is ${price}")
else:
    print("Tire price not available for the specified dimensions.")

# Asking the user if they want to buy tires for the specific dimension
buy_tires = input("Do you want to buy tires with the specified dimensions? (yes/no): ")

# Storing the user's phone number if they want to buy tires
if buy_tires.lower() == "yes":
    phone_number = input("Please enter your phone number: ")
    with open("volumes.txt", "a") as file:
        file.write(f"{phone_number}\n")
        print()
elif  buy_tires.lower() == "no":
        print("Thank you")



