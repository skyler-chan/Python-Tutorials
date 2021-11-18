# First basic project Weight Converter Program (correct!) - troubleshooted - remember to include the () after the dot operator

weight = int(input("What is your weight? "))
type = input("(l)bs or (k)g: ")

if type.upper() == "L":
    converted_weight = weight * 0.45
    print(f"You are {converted_weight} kilograms.")

else:
    converted_weight = weight / 0.45
    print(f"You are {converted_weight} pounds.")
