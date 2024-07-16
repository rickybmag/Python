#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 15, 18, or 20? ")
people = input("How many people to split the bill? ")
bill_total = float(bill)
tip_total = (int(tip) / 100) + 1
bill_with_tip = round(bill_total * tip_total - bill_total,2)
people_total = int(people)
bill_final = (bill_total / people_total) * tip_total
bill_final = "{:.2f}".format(bill_final)

print(f"Your final bill, with tip, is ${bill_final}")
print(f"The tip amount was ${bill_with_tip}")
