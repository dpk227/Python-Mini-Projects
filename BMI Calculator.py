# BMI = Body mass in kg / (Height in meter)^2
# Create a platform to calculate BMI
fname = input("Enter your first name: ")
print("Hello " + fname + '!')
yage = int(input("Please enter your age: "))
weight_kg = int(input("Please enter your weight in 'Kg': "))
if weight_kg == 0:
    weight_kg = int(input("Please enter your valid weight in 'Kg': "))
weight = weight_kg * 2.20462
height = int(input("Enter your Height in 'inches': "))
if height < 12:
    height = int(input("Please enter your valid height in 'inches': "))
bmi = (703 * weight)/(height**2)
print("----------BMI Result----------")
print("Name: " + fname)
print("Age: ", yage)
print("Height (inches): ", height)
print("Weight (Kg): ", weight_kg)
print("BMI Score: " + "{:.2f}".format(bmi))
if bmi > 0:
    if bmi < 18.5:
        print("Remark: " + fname + ", Sorry!!, you're Underweight.")
    if 18.5 < bmi < 25:
        print("Remark: " + fname + ", WOW!, your weight is normal.")
    if 25 < bmi < 30:
        print("Remark: " + fname + ", Ohh!, you're overweight.")
    if 30 < bmi < 35:
        print("Remark: " + fname + ", You have 'Obsese class 1' overweight")
    if 35 < bmi < 40:
        print("Remark: " + fname + ", You have 'Obsese class 2' overweight")
    if bmi > 40:
        print("Remark: " + fname + ", You have 'Obsese class 3' overweight")
else:
    print("Remark: " + "Please enter valid details.")
