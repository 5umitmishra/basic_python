# TODO User will input (3ages).Find the oldest one
a = int(input("enter your age "))
b = int(input("enter another age "))
c = int(input(("enter another age ")))

if a > b and a > c:
    print(" a is greater")
elif b > a and b > c:
    print("b is greater")
else:
    print("c is greater")

# TODO Write a program that will convert celsius value to fahrenheit
n = int(input("enter temperature in °C "))
fahrenheit = (n * (9/5)) + 32
print(fahrenheit)

# TODO User will input (2numbers).Write a program to swap the numbers
a = input("enter a number")
b = input("enter a another number ")
c = a
a = b
b = c
print(a)
print(b)

a,b = b,a
print(a)
print(b)

# TODO Write a program that will give you the sum of 3 digits
num = int(input("enter 3 digit number"))

a = num // 100
b = (num // 10) % 10
c = num % 10
sum = (a + b + c)
print(sum)

a = 123 // 100
print(a)
b = (123 // 10) % 10
print(b)
c = 123 % 10
print(c)
sum = a + b + c
print("the sum of 3 digit no. is: ",sum)

# TODO Write a program that will reverse a four digit number.Also it checks whether the reverse is true.
i = int(input("input: "))
rev = 0
while i > 0:
    rev = (rev * 10) + i % 10
    i = i // 10
print(rev)
if i == rev:
    print("true")
else:
    print("false")



# TODO Write a program that will tell whether the number entered by the user is odd or even.
n = int(input('enter a number '))
if n % 2 == 0:
    print("even number ")
else:
    print("odd number ")


# TODO Write a program that will tell whether the given year is a leap year or not.
n = int(input('enter a number '))
if n % 4 == 0:
    print("leap year ")
else:
    print("Not a leep year ")

# TOdo Write a program to find the euclidean distance between two coordinates.
x_1 = float(input("enter x1 cordinates"))
y_1 = float(input("enter y1 cordinates"))
x_2 = float(input("enter x2 cordinates"))
y_2 = float(input("enter y2 cordinates"))

d = ((x_2 - x_1)** 2 + (y_2 - y_1)**2)** 0.5
print(d)


# Todo Write a program that take a user inputr of three angles and will find out whether it can form a triangle or not.
a = int(input("enter side A "))
b = int(input("enter side B "))
c = int(input("enter side C "))

if a + b > c:
    print("it is a tringle")
else:
    print("not a tringle ")


# TOdo Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit
cost = int(input("what is cost prise "))
sell = int(input("what is celling prise "))

if cost > sell:
    print("you're in profit ")
else:
    print("you're in loss ")



