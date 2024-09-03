input = float(input("Input Distance in Kilometers: "))

def convert_distance(number):
    return input / 1.609344 # 1 mile = 1.609344 km so we divide to get result

print(f"Distance in Miles: {convert_distance(number = input)}")