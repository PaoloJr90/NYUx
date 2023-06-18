w = int(input("Please enter weight in kilograms: "))
h = float(input("Please enter height in meters: "))

BMI = round((w/(h**2)),2)

if (0 < BMI < 18.5):
    print("BMI is: ", BMI,",", " Status is Underweight", sep="")
elif(18.5 <= BMI <= 24.9):
    print("BMI is: ", BMI,",", " Status is Normal", sep="")
elif(25.0 <= BMI <= 29.9):
    print("BMI is: ", BMI,",", " Status is Overweight", sep="")
if(BMI >= 30.0):
    print("BMI is: ", BMI,",", " Status is Obese", sep="")

