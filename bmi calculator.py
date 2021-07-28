Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # BMI calculator using def
def body_mass_index(height,weight):
    bmi= weight / (height**2)
    return bmi

name=str(input("Enter your name: "))
height= float(input("Enter your height in meter: "))
weight= float(input("Enter your weight in kg: "))
bmi=body_mass_index(height, weight)
print("HI,",name)
print("Your BMI is", format(round(bmi,2)),"so your ", end='')
if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 24.9:
    print("Healthy")
elif 24.9 <= bmi < 30:
    print("overweight")
elif bmi >= 30:
    print("suffering from obesity")


# Thanks for watching
# Like, Share & Subscribe to
# Dream 2 Code
