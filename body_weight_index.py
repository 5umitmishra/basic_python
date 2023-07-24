

#bmi calculator 2.0

hight = float(input("enter your hight in m: "))
weight = int(input("enter your weight kg: "))

bmi_a =  (weight) / (hight) ** 2

bmi = int(bmi_a)

#print(type(bmi))

if bmi <=18:
    print(f"your bmi is {bmi}, you're underweight" )
elif bmi <=22:
    print(f"Your bmi is {bmi}, you have a normal weight")
elif bmi <=28:
    print(f"your bmi is {bmi},you are slightly overweight.")
elif bmi <= 33:
    print(f"your bmi is {bmi}, you are obsese.")
else:
    print(f"your bmi is {bmi},you are clinically obese. ")
