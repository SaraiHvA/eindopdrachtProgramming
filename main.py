from datetime import datetime
from datetime import date


# Calculate gross-net salary

# This class validates the input from the user
class Validation:

    # This function validates the birthday
    # Example valid birthday 01-01-1990
    def validateBirthday(inputBirthday):
        try:
            datetime.strptime(str(inputBirthday), '%d-%m-%Y')
            return inputBirthday
        except ValueError:
            print(str(inputBirthday) + f' is geen geldige geboortedatum, geef een geldige datum op, die een d-m-Y '
                                       f'formaat heeft.')

    # This function validates the period
    # Expects the input is an item from the given list
    def validatePeriodList(inputPeriodList: str):
        if inputPeriodList in periodList:
            return inputPeriodList
        else:
            print(str(inputPeriodList) + f' is geen geldige loonperiode, kies een loonperiode uit de lijst.')

    # This function validates the full-time hours
    # Expects the input is an item from the given list
    def validateFulltimeList(inputFulltimeList: str):
        fulltimeInt = int(inputFulltimeList)
        if fulltimeInt in fulltimeList:
            return fulltimeInt
        else:
            print(str(fulltimeInt) + f' is geen geldige keuze, kies een optie uit de lijst.')

    # This function validates the working hours per week
    # Expect the input to be greater than 0 and less than or equal to 168
    def validateWorkingHours(inputHours: int):
        if int(inputHours) and 40 >= int(inputHours) > 0:
            return inputHours
        else:
            print(str(inputHours) + f' is geen geldige invoer, geef het juiste aantal uren per week op voor een '
                                    f'fulltime werkweek.')

    # This function validates the hours for a fulltime working week
    # Expect the input to be greater than 0 and less than or equal to the given input hours
    def validateWorkingHoursWeek(inputHoursWeek: int):
        if int(inputHoursWeek) and int(hours) > int(inputHoursWeek) > 0:
            return inputHoursWeek
        else:
            print(str(inputHoursWeek) + f' is geen geldige invoer, geef het juiste gewerkte uren per week op.')

    # This function validates the try again answer
    # Expects the input is an item from the given list
    def validateTryAgainList(inputTryAgainList: str):
        if inputTryAgainList in tryAgainList:
            return inputTryAgainList
        else:
            print(str(inputTryAgainList) + f' is geen geldige keuze, kies ja of nee.')

# This function calculates the age of the user
# Calculates the age from the given birthday
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

# This function calculates the income
def calculateIncome(birthday, period, hours, hoursWeek):
    anwserIncome = Calculate.calculateBirthday(birthday)
    anwserFulltime = Calculate.calculateFullTimeHours(hours, anwserIncome)
    answerHours = Calculate.calculateHours(hoursWeek, hours, anwserFulltime)
    answer = Calculate.giveDesiredResult(period, answerHours)
    return answer

# In this class are functions that calculates the income step by step
class Calculate:

    # This function gets the minimum income for a 40 hour working week with the given age
    def calculateBirthday(birthday):
        if birthday >= 21:
            income = 9.72
            return income
        elif birthday == 20:
            income = 7.78
            return income
        elif birthday == 19:
            income = 5.84
            return income
        elif birthday == 18:
            income = 4.86
            return income
        elif birthday == 17:
            income = 3.84
            return income
        elif birthday == 16:
            income = 3.36
            return income
        elif birthday <= 15:
            income = 2.92
            return income

    # This function calculates the minimum income of the given full-time working week
    def calculateFullTimeHours(hours, income):
        if(hours == 38):
            newIncome = income / 5
            return newIncome
        elif(hours == 36):
            newIncome = income / 2
            return newIncome
        else:
            return income

    # This function calculates the minimum income of the given weekly work hours
    def calculateHours(hoursWeek, hours, income):
        # print(income, hours, hoursWeek)
        newIncome = int(income) / int(hours) * int(hoursWeek)
        return newIncome

    # This function returns the income to the desired result
    def giveDesiredResult(period, income):
        if(period == 'maand'):
            return income
        elif(period == 'dag'):
            newIncome = income / 31
            return newIncome
        elif(period == 'week'):
            newIncome = income / 31 * 7
            return income
        elif(period == 'jaar'):
            newIncome = income / 31 * 365
            return newIncome
        return

while True:
    print("Minimum loon berekenen.")

    # This while and if statement handles the input validation for the birthday and returns the age when true
    while True:
        birthdayInput = input("Enter geboortedatum: ")
        if not Validation.validateBirthday(birthdayInput):
            continue
        else:
            dob = datetime.strptime(birthdayInput, '%d-%m-%Y')
            birthday = calculate_age(dob)
            break

    # This while and if statement handles the input validation for the period and returns it when true
    while True:
        # periodList = ["maand", "dag", "week", "4 weken", "kwartaal", "jaar", "alle"]
        periodList = ["maand", "dag", "week", "jaar"]
        print(periodList)
        payPeriod = input("Kies de gewenste minimum loon berekening: ")
        if not Validation.validatePeriodList(payPeriod):
            continue
        else:
            period = payPeriod
            break

    # This while and if statement handles the input validation for the full-time hours and returns when true
    while True:
        fulltimeList = [36, 38, 40]
        print(fulltimeList)
        # print(', '.join(fulltimeList))
        hoursInput = input("Kies een fulltime werkweek in uw branche of sector uit de lijst hierboven: ")
        if not Validation.validateFulltimeList(hoursInput):
            continue
        else:
            hours = hoursInput
            break

    # This while and if statement handles the input validation for the worked hours in the week and returns when true
    while True:
        hoursWeekInput = input("Aantal uur dat u per week werkt: ")
        if not Validation.validateWorkingHoursWeek(hoursWeekInput):
            continue
        else:
            hoursWeek = hoursWeekInput
            break

    # This if statement checks result and returns the net salary
    result = calculateIncome(birthday, period, hours, hoursWeek)
    if result:
        print("Uw netto " + period + " salaris is: ")
        print(result)

    # This if statement checks the in
    tryAgainList = ["ja", "nee"]
    tryAgain = input("Wilt u opnieuw een bruto-netto berekening doen?")
    if tryAgain == 'ja':
        continue
    else:
        break
