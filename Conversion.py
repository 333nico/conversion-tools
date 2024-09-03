choose_tool = int(input("Choose a conversion tool (1 for KM to miles, 2 for °C to °F, 3 for binary to decimal): "))

def convert_distance(number):
    return input / 1.609344 # 1 mile = 1.609344 km so we divide to get result

def convert_temp(number):
    return (input * 1.8) + 32 # fahrenheit = celsius x 1.8 + 32

if choose_tool == 1:
    input = float(input("Input Distance in Kilometers: "))
    print(f"Distance in Miles: {convert_distance(number = input)} mile(s)")
if choose_tool == 2:
    input = float(input("Input Temperature in Celsius: "))
    print(f"Temperature in Fahrenheit: {convert_temp(number = input)} °F")
