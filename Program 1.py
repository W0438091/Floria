#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Floria Jung
Program Title:  Hipster's Local Vinyl Records 
Description:    This program will generate customer's receipts. It will display the customer's name and 3 calculated costs: 
                delivery ost, reords cost (plus tax) and total cost. 
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    #1. Program start
    print("Welcome to Hipster's Local Vinyl Records")

    #2. Create variables for delivery rate, sales tax, number of km distance, and the cost of any records purchased.
    #Variables
    deliveryRate = 15
    salesTax = 1.14
    distance = 0.0 
    costOfRecords = 0.0

    #3. Ask the user to enter the name, distance in km, and the cost of records. 
    #INPUT
    customerName = input("Please write your name: ")
    distance = input("Please enter the distance in kilometer: ")
    costOfRecords = input("Please enter the cost: ")

    #Processing
    deliveryRate = 15
    salesTax = 1.14
    deliveryCost = float(distance)* int(deliveryRate)
    purchaseCost = float(costOfRecords) * float(salesTax)
    totalCost = deliveryCost + purchaseCost

    #OUTPUT
    print("Purchase summary for: ", customerName)
    print("Your Delivery Cost is: $", deliveryCost)
    print("Your Purchase Cost is: $", purchaseCost)
    print("Your Total Cost is: $",totalCost )

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()

 