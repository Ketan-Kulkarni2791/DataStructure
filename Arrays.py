# In feb how many dollars have you spent extra as compared to January ?
def JanComparedToFeb(months, money):
    ExtraMoneySpent = money[1] - money[0]
    print(ExtraMoneySpent)


# Find out your total expense in first quarter of the year
def FirstQuarterExpense(money):
    print('{}'.format(money[0] + money[1] + money[2]))


# If you have spent exactly 2000 dollars in any month
def ExactAmountSpent(months, money):
    # for i in money:
    if 2000 in money:
        print('Spent.')
    else:
        print("No 2000 dollars spent in any month.")


# June month is finished. Add your expense of 1980 ti array.
def AddJune(months, money):
    months.append('June')
    money.append(1980)
    print(months + money)


# You returned a item you bought in month of April, and got a refund of $200
def Correction(money):
    money[3] = money[3] - 200
    print('Updated : ', money)


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
money = [2200, 2350, 2600, 2130, 2190]
JanComparedToFeb(months, money)
FirstQuarterExpense(money)
ExactAmountSpent(months, money)
AddJune(months, money)
Correction(money)
