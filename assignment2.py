"""
### Assignment 2
#### Calculation of an investment with a recurring deposit
The simple interest formula only works if the principal or initial investment is not touched.  If an amount is added to the principal every year, then the interest must be calculated and added along with the future deposit to determine the starting balance at the beginning of the next year.

For example, suppose you invest $100 every year, and earn 5% interest per year.
At the start of the first year, you will have your $100 that you invested.  At the start of the second year, you will have the initial $100, $5 interest as well as an additional $100 that is invested in the second year, for a total of $205 dollars.  Write a program that uses a for loop to determine the amount of money in an account after a certain number of years.

Criteria:
Your program should ask the user for
* the annual investment
* the annual interest rate (as a percentage)
* the number of years
* calculate the amount of money at the end of each year until the specified number of years has been reached.
* appropriate formatting and variable names will be important
* use a *for* loop to iterate through the years.

Sample data
annual investment: 100
rate: 5%
10 years
final balance: 1320.68

"""

while True:
  try:
    intin=input("Enter the annual investment: ")
    intin=float(intin)
    assert intin>0
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
  Time = input('\nHow long will the investment be in years.\nEnter value as a whole number: ')
  try:
    Time = int(Time)
    assert Time>0
    break
  except:
    print("Invalid Value.\nTry again.")

x=intin

for i in range(Time):
  x=x+x*rate/100
  x=round(x,2)
  print(f'Year {i+1}, Money=${x}\n')
  x=x+intin