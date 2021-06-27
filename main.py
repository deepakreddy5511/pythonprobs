weight = int(input("Weight:"))
unit = input("Enter LBS or KGS:")
if unit == "LBS":
    convert = weight * 0.45
    print(f'you are {convert} KGS')
else:
    convert = weight / 0.45
    print(f'you are {convert} LBS')