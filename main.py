# Sarai Misidjan
# Calculate your minimum wage or minimum youth wage per month, week, day, hour and year.
# This applies to a full-time or part-time job. This will give you an idea of the minimum you should earn.
# The minimum wage depends on the full-time working week at your employer.
# With a full-time job, for example, this is 36, 38 or 40 hours.
from datetime import datetime
from datetime import date
import math


# This class validates the input from the user
from numbers import Number


class Validation:

    # This function validates the birthday
    # Example valid birthday 01-01-1990
    def validateBirthday(self, inputBirthday):
        try:
            datetime.strptime(str(inputBirthday), '%d-%m-%Y')
            return inputBirthday
        except ValueError:
            print('Fout: ', str(inputBirthday) + f' is geen geldige geboortedatum, geef een geldige datum op, die een '
                                                 f'd-m-Y formaat heeft.')

    # This function validates the period
    # Expects the input is an item from the given list
    def validatePeriodList(self, inputPeriodList: str):
        if inputPeriodList in periodList:
            return inputPeriodList
        else:
            print('Fout: ', str(inputPeriodList) + f' is geen geldige loonperiode, kies een loonperiode uit de lijst.')

    # This function validates the full-time hours
    # Expects the input is an item from the given list
    def validateFulltimeList(self, inputFulltimeList: int):
        if int(inputFulltimeList) in fulltimeList:
            return int(inputFulltimeList)
        else:
            print('Fout: ', int(inputFulltimeList) + f' is geen geldige keuze, kies een optie uit de lijst.')

    # This function validates the working hours of the user per week
    # Expect the input to be greater than 0 and less than or equal to the given full-time hours of your employer
    def validateWorkingHoursWeek(self, inputHoursWeek: int):
        if int(inputHoursWeek) and int(hours) >= int(inputHoursWeek) > 0:
            return inputHoursWeek
        else:
            print('Fout: ', str(inputHoursWeek) + f' is geen geldige invoer, geef het juiste gewerkte uren per week op.')

    # This function validates the try again answer
    # Expects the input is an item from the given list
    def validateTryAgainList(self, inputTryAgainList: str):
        if inputTryAgainList in tryAgainList:
            return inputTryAgainList
        else:
            print('Fout: ', str(inputTryAgainList) + f' is geen geldige keuze, kies ja of nee.')


# This function calculates the age of the user
# Calculates the age from the given birthday
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


# This function calculate your minimum wage or minimum youth wage
def calculateIncome(Calculate, age: int, hoursFullTime: int, hoursWeek: int, period: str):
    anwserAge = Calculate.calculateIncomeWithBirthday(Calculate, age)
    anwserFulltime = Calculate.getIncomeFullTimeHours(Calculate, hoursFullTime, anwserAge)
    answerHours = Calculate.calculateHours(Calculate, hoursWeek, hoursFullTime, anwserFulltime)
    answerIncome = Calculate.giveDesiredResult(Calculate, period, answerHours)
    answer = Calculate.roundIncomeOff(Calculate, answerIncome)
    return answer


# In this class are functions that calculates the minimum wage step by step
class Calculate:
    day = 8  # hours
    week = 7  # days
    month = 31  # days
    year = 365  # days

    # This is a dict of the minimum wage for a certain age for a 40 hour working week
    minimumWageFortyHours = {
        21: 9.72,
        20: 7.78,
        19: 5.84,
        18: 4.86,
        17: 3.84,
        16: 3.36,
        15: 2.92
    }

    # This is a dict of the minimum wage for a certain age for a 38 hour working week
    minimumWageThirtyEightHours = {
        21: 10.24,
        20: 8.19,
        19: 6.14,
        18: 5.12,
        17: 4.05,
        16: 3.54,
        15: 3.07
    }

    # This is a dict of the minimum wage for a certain age for a 36 hour working week
    minimumWageThirtySixHours = {
        21: 10.80,
        20: 8.65,
        19: 6.49,
        18: 5.40,
        17: 4.27,
        16: 3.73,
        15: 3.25
    }

    # If the age is above 21 years the minimum wage remains the same
    # If the age is under 15 years the minimum wage remains the same
    # This function returns the age
    def calculateIncomeWithBirthday(self, age: int):
        if age > 21:
            age = 21
            return age
        elif age < 15:
            age = 15
            return age
        return age

    # This function gives the minimum wage of the given full-time working week at your employer
    # Expects the age and full-time working week at your employer
    def getIncomeFullTimeHours(self, hoursFullTime: int, age: int):
        if hoursFullTime == 40:
            income = self.minimumWageFortyHours.get(age)
            return income
        elif hoursFullTime == 38:
            return self.minimumWageThirtyEightHours.get(age)
        elif hoursFullTime == 36:
            return self.minimumWageFortyHours.get(age)
        else:
            return self.minimumWageFortyHours.get(age)

    # This function calculates the minimum wage of the given weekly hours the user is working
    def calculateHours(self, hoursWeek: int, hoursFulltime: int, income: float):
        newIncome = float(income) / int(hoursFulltime) * int(hoursWeek)
        return newIncome

    # This function returns the income to the desired result:
    # "maand", "dag", "week", "jaar", "uur"
    def giveDesiredResult(self, period: str, income: float):
        incomeDay = float(income) * self.day
        if (period == 'uur'):
            return income
        elif (period == 'dag'):
            return float(incomeDay)
        elif (period == 'maand'):
            newIncome = float(incomeDay) * self.month
            return newIncome
        elif (period == 'week'):
            newIncome = float(incomeDay) * self.week
            return newIncome
        elif (period == 'jaar'):
            newIncome = float(incomeDay) * self.year
            return newIncome
        return

    # This function returns the income with 2 decimals after the comma
    # This only applies if the income has more than 2 decimal places after the comma
    def roundIncomeOff(self, income):
        result = str(income)
        roundedResult = round(income, 2)
        return int(roundedResult)


while True:
    print("Rekenhulp: minimumloon berekenen")
    print()
    print("Bereken uw minimumloon of minimumjeugdloon per maand, week, dag, uur en jaar.")
    print("Dit geldt voor een fulltime of parttime baan. Zo krijgt u een idee van wat u minimaal hoort te verdienen.")
    print("Het minimumloon hangt af van de fulltime werkweek bij uw werkgever. Dit is bij een fulltime baan "
          "bijvoorbeeld 36, 38 of 40 uur.")
    print()
    print("Vul uw gegevens in en bereken uw minimumloon.")
    print()

    # The while loop causes the question to be asked again if an incorrect answer is given
    while True:
        print("Vul je geboortedatum op deze manier in: 01-01-1990")
        birthdayInput = input("Enter geboortedatum: ")
        print()
        # If statement handles the input validation for the birthday
        # If false then the question will be asked again.
        # If true, the given birthday is converted to the user's age
        if not Validation.validateBirthday(Validation, birthdayInput):
            continue
        else:
            dob = datetime.strptime(birthdayInput, '%d-%m-%Y')
            age = calculate_age(dob)
            break

    # The while loop causes the question to be asked again if an incorrect answer is given
    while True:
        periodList = ["maand", "dag", "week", "jaar", "uur"]
        print('Loon per: ', periodList)
        payPeriod = input("Hoe wilt u uw minimum loon terug krijgen? Kies uit de lijst hierboven: ")
        print()
        # This if statement handles the input validation for the period
        # If false then the question will be asked again
        # If true, the given pay period is set.
        if not Validation.validatePeriodList(Validation, payPeriod):
            continue
        else:
            period = payPeriod
            break

    # The while loop causes the question to be asked again if an incorrect answer is given
    while True:
        fulltimeList = [36, 38, 40]
        print(fulltimeList, 'uur')
        hoursInput = input("Kies de fulltime werkweek per uur in uw branche of sector uit de lijst hierboven: ")
        print()
        # This if statement handles the input validation for the full-time hours at the employer
        # If false then the question will be asked again
        # If true, the given full-time hours at your employer is set
        if not Validation.validateFulltimeList(Validation, hoursInput):
            continue
        else:
            hours = hoursInput
            break

    # The while loop causes the question to be asked again if an incorrect answer is given
    while True:
        print("Geef het aantal uren dat jij per week werkt, bijv. 30")
        hoursWeekInput = input("Aantal uur dat u per week werkt: ")
        print()
        # This if statement handles the input validation for the hours the user is working per week
        # If false then the question will be asked again
        # If true, the given weekly worked hours is set
        if not Validation.validateWorkingHoursWeek(Validation, hoursWeekInput):
            continue
        else:
            hoursWeek = hoursWeekInput
            break

    # This method calculates the minimum wage with the given input from the user and returns the result
    result = calculateIncome(Calculate, age, hours, hoursWeek, period)
    # This if statement checks if result is set and prints the minimum wage in the given period the user gave.
    if result:
        roundedResult = round(result, 2)

        print("Uw minimum loon per " + period + " is: %s" % u"\N{euro sign}", roundedResult)
        print()

    # The while loop causes the question to be asked again if an incorrect answer is given
    while True:
        tryAgainList = ["ja", "nee"]
        print("Keuze: ", tryAgainList)
        tryAgain = input("Wilt u een ander minimum loon berekenen / wilt u opnieuw beginnen?")
        # This if statement handles the input validation - if the choice is 'ja' or 'nee'
        # If returned false then the question will be asked again
        # Else you continue to the next if statement within the while
        if not Validation.validateTryAgainList(Validation, tryAgain):
            continue
        # This if statement checks if the choice is 'ja' or 'nee'
        # If returned false then the question will be asked again
        # Else you continue to the next if statement outside of the while
        if tryAgain == 'ja' or tryAgain == 'nee':
            break
        else:
            continue

    # This if statement check if the input is 'nee'
    # If returned true, you get a massage and the application stops
    if tryAgain == 'nee':
        print("Bedankt en tot ziens!")
        break
