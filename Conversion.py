print("Week 2 Lab project\nOption 1 - KM to Miles\nOption 2 - Celsius to Fahrenheit\nOption 3 - Binary to Decimal")
chooseTool = int(input("Choose a conversion tool: "))

def convert_distance(number):
    return number / 1.609344 # 1 mile = 1.609344 km so we divide to get result

def convert_temp(number):
    return (number * 1.8) + 32 # fahrenheit = celsius x 1.8 + 32

def convert_binary(number):
    return int(str(number), 2) # returns base 2 number as a decimal number

if chooseTool == 1:
    input = float(input("Input Distance in Kilometers: "))
    print(f"Distance in Miles: {convert_distance(number = input)} mile(s)")
if chooseTool == 2:
    input = float(input("Input Temperature in Celsius: "))
    print(f"Temperature in Fahrenheit: {convert_temp(number = input)} °F")
if chooseTool == 3:
    input = input("Input Number in Binary: ")
    print(f"Number in Decimal: {convert_binary(number = input)}")
