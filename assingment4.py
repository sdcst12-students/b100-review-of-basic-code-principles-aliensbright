"""
### Assignment 4
#### Calculation of a debt repayment with recurring payments
This is the reverse of assignments 2 and 3

Calculate how long it will take to completely pay off a debt if regular payments are made.  Note that each year, the debt will increase by the amount of loan interest, but will decrease with youre recurring payment. 

Criteria:
Your program should ask the user for
* an initial debt
* the annual interest rate
* the annual payment
* the program will state how long it will take for the debt to be repaid.
* extra: Calculate the total amount of interest that is paid along with the debt repayment

Sample:
Joey takes a car loan to buy a new Tesla for $62000
The loan has an annual interest rate of .75% per month.  He makes monthly payments of $1000.
How many months will it take him to pay off the car.  How much interest has he paid in that time?

84 months
He will have paid 21711.60 in interest
"""

while True:
  try:
    debt=input("Enter the initial debt: ")
    debt=float(debt)
    assert debt>0
    break
  except:
    print('Invalid value.\nTry again')

while True:
  try:
    rate=input('\nEnter the interest rate as a percentage.\nOnly enter a number: ')
    rate=float(rate)
    assert rate<100
    assert rate>0
    break
  except:
    print('\nInvalid value.\nTry again')

while True:
  repay = input('\nEnter the annual repayment.\nEnter value as a whole number: ')
  try:
    repay = float(repay)
    assert repay>0
    break
  except:
    print("Invalid Value.\nTry again.")
new=debt
years=0
while new>0:
  new=new-(debt-repay)*rate/100
  new=round(new,2)
  years=years+1

print(f"\nTotal repayment : ${repay*years}")
print(f"\nTotal interest paid : ${repay*years-debt}")
print(f"\nIt will take {years} years to repay the debt\n")
