name = input("NAME: ")
a = float(input("Height in meters: "))
b = float(input("Weight in kg: "))

if name.strip() == "":
    print("Enter a valid name.")
elif a <= 0 or b <= 0:
    print("Enter valid height and weight.")
else:
    bmi = b / (a ** 2)
    if bmi < 18.5:
        print(f"{name}, you are underweight with a BMI of {bmi:.2f}.")
    elif 18.5 <= bmi < 24.9:
        print(f"{name}, you have a normal weight with a BMI of {bmi:.2f}.")
    elif 25 <= bmi < 29.9:
        print(f"{name}, you are overweight with a BMI of {bmi:.2f}.")
    else:
        print(f"{name}, you have obesity with a BMI of {bmi:.2f}.")
