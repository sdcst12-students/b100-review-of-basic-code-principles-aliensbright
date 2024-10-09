"""
### Assignment 1
#### Calculation of Simple Interest
The simple interest formula is I = P*r*t where I = the amount of interest, P is the principal or the amount invested, r is the interest rate per year (converted to a decimal) and t is the length of time in years.
Write a program that calculates the amount of simple interest for an investment.

Criteria:
Your program should ask the user for 
* an initial investment
* the annual interest rate as a percentage
* the length of time.
  * the user should have the option of entering in the length of time in years, months or days
* The program will calculate the amount of interest earned and display it.
* Appropriate formatting of the output is a requirement for this assignment
"""

while True:
  try:
    intin=input("Enter the initial investment: ")
    intin=float(intin)
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
  LoT = input('\nWill the time be measured in years, months, or days. \nEnter Y for years, M for months, and D for days: ')
  LoT = LoT.lower()
  if LoT=="y":
    t=1
    break
  elif LoT=="m":
    t=12
    break
  elif LoT=="d":
    t=365
    break
  else:
    print("Invalid Value.\nTry again.")

while True:
  Time = input('\nHow long will the investment be.\nEnter value as a number: ')
  try:
    Time = float(Time)
    assert Time>0
    break
  except:
    print("Invalid Value.\nTry again.")



A = intin*(rate/100)*Time/t
A = round(A,2)
print('The total amount of interest earned is $',A)
print(f'\nYour total amount will be ${A+intin}')