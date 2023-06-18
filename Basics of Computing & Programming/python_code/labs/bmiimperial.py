w = float(input("Please enter weight in pounds: "))
h = float(input("Please enter height in inches: "))

k = w * 0.453592
m = h * 0.0254

BMI = (k/(m**2))

print("BMI is:", BMI)
