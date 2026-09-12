# inchi to centimeter

def inch_to_cms(inch):
    return inch * 2.54

inch = int(input("Enter length in inches: "))
cms = inch_to_cms(inch)
print(f"{inch} inch = {round(cms, 2)} cm")