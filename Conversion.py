print("Week 2 Lab project\nOption 1 - KM to Miles\nOption 2 - Celsius to Fahrenheit\nOption 3 - Binary to Decimal")
chooseTool = int(input("Choose a conversion tool: "))

def convert_distance(number):
    return number / 1.609344 # 1 mile = 1.609344 km so we divide to get result

def convert_temp(number):
    return (number * 1.8) + 32 # fahrenheit = celsius x 1.8 + 32

def convert_binary(number):
    binaryStr = str(number)
    decimal = 0 # store decimal number
    power = len(binaryStr) - 1 # keeps track of the pos of each digit
    
    for digit in binaryStr: # loop through each digit that = 1 and adds power of 2
        if digit == '1':
            decimal += 2 ** power
        power -= 1
    
    return decimal

if chooseTool == 1:
    input = float(input("Input Distance in Kilometers: "))
    print(f"Distance in Miles: {convert_distance(number = input)} mile(s)")
if chooseTool == 2:
    input = float(input("Input Temperature in Celsius: "))
    print(f"Temperature in Fahrenheit: {convert_temp(number = input)} °F")
if chooseTool == 3:
    input = input("Input Number in Binary: ")
    print(f"Number in Decimal: {convert_binary(number = input)}")
