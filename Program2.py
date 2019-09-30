#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:  Floria Jung    
Program Title:  Weekly Loan Calculator 
Description:    The program will calculate the weekkly payment with a given equation. 
                The user will enter the loan amount, the interest rate, and the number of years.
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    print("Weekly Loan Calulator")
    #Variables
    amountOfLoan = 0.0
    interestRate = 0.0
    numberOfYears = 0

    #PROCESSING
    #1. The user will interpret the math equation in words. 
    #2. If A dollars are borrowed at r perentage interest to purchase something with weekly paymetens for n years, 
    #   i = r / 5200 
    #3. Are there options you would like to enter? 
    #4. If yes, ask the user to enter the options. 

    #INPUT
    amountOfLoan = input("What is your amount of loan?: ")
    interestRate = input("What is your interest rate?: ")
    numberOfYears = int(input("What is the number of years?: "))

    #5. Calculate the total cost. <Description of math formula goes here> 
    #weekly payment = (i / 1 - (1 + i) ^ -52n) * A
    i = float(interestRate) / 5200 
    weeklyPayment = (i / (1 - (1 + i) ** (-52 * int(numberOfYears)))) * float(amountOfLoan)
    

    #OUTPUT
    #7. Display the final cost to the user.
    print("Enter the amount of loan: ", amountOfLoan)
    print("Enter the interest rate(%): ", interestRate)
    print("Enter the number of years: ", numberOfYears)
    print("Your weekly payment will be: $",weeklyPayment)
    outString = ("Your weekly payment will be: ${0:.2f}".format(weeklyPayment))
    print(outString)
    
    #8. Ask the user if they want to change any entered values?
    #answer = input("Would you like to change any values?")
    #if answer.upper() == "YES": 
    #        print("Go back to Step 3")
    #print("Mazel Tov!")
    
    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()