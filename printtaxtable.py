"""
Braxton Phillips
SDEV 220
Chapter 6 Excersice 6.15
Due Nov 7, 2020
"""
def taxCalculation(taxableIncome):

    if income <= 8350:
            tax = income * 0.10
    elif income <= 33950:
            tax = 8350 * 0.10 + (income - 8350) * 0.15
    elif income <= 82250:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
            (income - 33950) * 0.25
    elif income <= 171550:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
            (82250 - 33950) * 0.25 + (income - 82250) * 0.28
    elif income <= 372950:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
        (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
            (income - 171550) * 0.33
    else:
            tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
            (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
            (372950 - 171550) * 0.33 + (income - 372950) * 0.35;
    return(tax)

def computeTax(status, taxableIncome):
    if status == 0: #Compute tax for single filers
        tax *= 1
    elif status == 1: # Compute tax for married file jointly
        tax *= 2
        print('test')
    elif status == 2: # Compute tax for married separately
        tax *= 3
        print("Left as exercise")
    elif status == 3: # Compute tax for head of household
        tax *= 4
        print("Left as exercise")

    
def main():
    # Prompt the user to enter filing status
    status = eval(input("(0-single filer, 1-married jointly, 2-married separately, 3-head of household). Enter the filing status: "))

    # Prompt the user to enter taxable income
    income = eval(input("Enter the taxable income: "))

    tax =  computeTax(status, income)
    print(tax)
    print(computeTax_status, computeTax_income)


    main()