import string


height = int(input("Enter Your height in cm: "))
weight = int(input("Enter Your weight in kg: "))
BmiCategory = string
height = height/100
BMI = weight/(height*height)
print(BMI)
BMI100 = int(BMI*10)
if BMI100<160: BmiCategory = "Severe Thinness"
elif BMI100 in range(160, 170): BmiCategory = "Moderate Thinness"
elif BMI100 in range(170, 185): BmiCategory = "Mild Thinness"
elif BMI100 in range(185, 250): BmiCategory = "Normal"
elif BMI100 in range(250, 300): BmiCategory = "Overweight"
elif BMI100 in range(300, 350): BmiCategory = "Obese Class I"
elif BMI100 in range(350, 400): BmiCategory = "Obese Class II"
elif BMI100>400: BmiCategory = "Obese Class III"
print(f"Your BMI index is: {BMI}, You are in {BmiCategory} category")
