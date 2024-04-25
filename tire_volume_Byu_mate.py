from datetime import datetime

def calculate_tire_volume(width, aspect_ratio, wheel_diameter):
    pi = 3.14159
    volume = pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * wheel_diameter) / 10000000
    return volume / 1000

def main():
    # Get user input for tire specifications
    width = int(input("Enter the width of the tire in mm (ex 205): "))
    aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
    wheel_diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

    # Calculate tire volume
    volume = calculate_tire_volume(width, aspect_ratio, wheel_diameter)

    # Display the approximate volume
    print(f"The approximate volume is {volume:.2f} liters")

    # Get the current date
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Append values to the volumes.txt file
    with open("volumes.txt", "a") as file:
        file.write(f"{current_date}, {width}, {aspect_ratio}, {wheel_diameter}, {volume:.2f}\n")

if __name__ == "__main__":
    main()
