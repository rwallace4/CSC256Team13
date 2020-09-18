# Name: Rose Wallace
# Date: August 22, 2020
# Instructor: Tonya Melvin-Bryant
# File Name: RetirementAge.py
# Description: Program calculates a person'a retirement age and month/year of retirement after receiving month/year of birth from user. Displays calculations to screen
######################################################################################################################################################################################



import math


# Function: Main
# Parameters: none
# Variables: year, month, age_year, age_month
# Returns: none
# Description:  Calls the userInput function, the retirementAge function, the display function,
#               and the calculateDate function
#################################################################################################
def main():
    year, month = userInput()
    age_year, age_month = retirementAge(year)
    display(age_year, age_month)
    calculateDate(year, month, age_year, age_month)



# Function: userInput
# Parameters: none
# Variables: year, month
# Returns: year, month
# Description:  Receives user input for their month and year of birth, returns values to the main
#               function.
#################################################################################################
def userInput():
    year = int(input("Enter the year of birth or to press 'enter' to exit: "))
    month = int(input("Enter the month of birth: "))
    return year, month

# Function: retirementAge
# Parameters: year
# Variables: age_year, age_month
# Returns: age_year, age_month
# Description:  Calculates the number of years required for retirement and the number of months
#               as well from governemnt/social security website. Hard-coded.
#################################################################################################
def retirementAge(year):
    if year <= 1937:
        age_year = 65
        age_month = 0
    if 1937 < year < 1943:
        extra_months = 2 * (year-1937)
        age_year = 65 + int((extra_months/12))
        age_month = extra_months %12
    if 1943 <= year < 1955:
        age_year = 66
        age_month = 0
    if 1955 <= year < 1960:
        extra_months = 2 * (year-1954)
        age_year = 66 + int((extra_months)/12)
        age_month = extra_months %12
    if year >=1960:
        age_year = 67
        age_month = 0
    return age_year, age_month


# Function: display
# Parameters: age_year, age_month
# Variables: None
# Returns: none
# Description:  Displays the amount of time in years and months until the individual can retire.
#################################################################################################
def display(age_year, age_month):
    print("Your full retirement age is ", age_year, " and ", age_month, " months")

# Function: calculateDate
# Parameters: year, month, age_year, age_month
# Variables: retirement_year, retirement_month, final_month
# Returns: none
# Description:  Determines the specific month and year of retirement for the individual and
#               displays both on the console.
#################################################################################################
def calculateDate(year, month, age_year, age_month):
    retirement_year = year + age_year
    retirement_month = month + age_month
    if retirement_month > 12:
        retirement_year = retirement_year + 1
        retirement_month = retirement_month % 12
    if retirement_month == 1:
        final_month = "January"
    elif retirement_month == 2:
        final_month = "February"
    elif retirement_month == 3:
        final_month = "March"
    elif retirement_month == 4:
        final_month = "April"
    elif retirement_month == 5:
        final_month = "May"
    elif retirement_month == 6:
        final_month = "June"
    elif retirement_month == 7:
        final_month = "July"
    elif retirement_month == 8:
        final_month = "August"
    elif retirement_month == 9:
        final_month = "September"
    elif retirement_month == 10:
        final_month = "October"
    elif retirement_month == 11:
        final_month = "November"
    elif retirement_month == 12:
        final_month = "December"

    print("This will be in ", final_month, " of ", retirement_year)

# Calls the main function
main()

