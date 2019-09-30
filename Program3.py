#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Floria jung
Program Title:  Imperial to Metric Conversion 
Description:    This program will convert impterial units to metric units. The user will enter the number of tons, stones, pounds, and ounces. 
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    print("Welceome to Metric Conversion Program")

    #VARIABLES
    tons = 0
    stones = 0
    pounds = 0
    ounces = 0
    grams = 0.0 

    #INPUT
    numOfTons = input("What is the number of tons?: ")
    numOfStones = input("What is the number of stones?: ")
    numOfPounds = input("What is the number of pounds?: ")
    numOfOunces = input("What is the number of ounces?: ")

    #PROCESSING
    #1. Convert all the weights into ounces
    stone = 224 * int(numOfStones)
    pound = 16 * int(numOfPounds)
    ton = 35840 * int(numOfTons)

    #2. Calculate total ounces
    totalOunces = int(stone) + int(pound) + int(ton) + int(numOfOunces)
    
    #3. Caculate correct value of tons.
    totalKilos = int(totalOunces) / 35.274
    metricTons = int(totalKilos) / 1000
    valueTons = int(metricTons)

    #3. Calculate correct value of kilos. 
    kiloValue = int(totalKilos - (int(metricTons) * 1000))

    #4. Calvulate correct value of grams. 
    metricGrams = (totalKilos - (int(totalKilos))) * 1000

    #OUTPUT
    outString = "The metric weight is {0} metric tons, {1} kilos, and {2:.1f} grams.".format(valueTons, kiloValue, metricGrams)
    print(outString)

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()