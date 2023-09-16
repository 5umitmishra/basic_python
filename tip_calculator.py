


#tip calculator

print("welcome to the tip calculator ")

bill = float(input("what was the total bill "))

tip = int(input("what percentage tip would you like to give ? 10, 12,or 15 "))

split = int(input("how many people to split the bill "))

add_tip = (tip/100*bill)

final_bill = bill + add_tip

splite_bill = final_bill / split

spliting= round(splite_bill,2)

spliting = "{:.2f}".format(splite_bill)

print(f"each person should pay {spliting}")
