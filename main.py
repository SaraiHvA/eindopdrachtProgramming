from datetime import datetime
from datetime import date


# Program make a simple calculator

# This class validates the input from the user
class Validation:

    # This function validates the birthday
    # Example valid birthday 01-01-1990
    def validateBirthday(inputBirthday):
        try:
            datetime.strptime(str(inputBirthday), '%d-%m-%Y')
            return inputBirthday
        except ValueError:
            print(str(inputBirthday) + f' is geen geldige geboortedatum, geef een geldige datum op, die een d-m-Y formaat heeft.')

    # This function validates the period
    # Expects the input is an item from the given list
    def validateList(input: str):
        if input in periodList:
            return input
        elif input in fulltimeList:
            return input
        else:
            print(str(input) + f' is geen geldige loonperiode, kies een loonperiode uit de lijst.')

    # This function validates the working hours per week
    # Expect the input to be greater than 0 and less than or equal to 168
    def validateWorkingHours(input: int):
        if int(input) and 40 >= int(input) > 0:
            return input
        else:
            print(str(input) + f' is geen geldige invoer, geef het juiste aantal uren per week op voor een fulltime werkweek.')

    # This function validates the hours for a fulltime working week
    # Expect the input to be greater than 0 and less than or equal to the given input hours
    def validateWorkingHoursWeek(input: int):
        if int(input) and int(hours) > int(input) > 0:
            return input
        else:
            print(str(input) + f' is geen geldige invoer, geef het juiste gewerkte uren per week op.')


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


# This class calculates the minimum wage
class Calculate:

    def calculateIncome(self, birthday, period, hour, hourWeek):
        if birthday >= 21:
            income = 9.72
        elif birthday == 20:
            income = 7.78
        elif birthday == 19:
            income = 5.84
        elif birthday == 18:
            income = 4.86
        elif birthday == 17:
            income = 3.84
        elif birthday == 16:
            income = 3.36
        elif birthday <= 15:
            income = 2.92


print("Minimum loon berekenen.")

while True:

    while True:
        birthdayInput = input("Enter geboortedatum: ")
        if not Validation.validateBirthday(birthdayInput):
            continue
        else:
            dob = datetime.strptime(birthdayInput, '%d-%m-%Y')
            birthday = calculate_age(dob)
            break

    while True:
        periodList = ["maand", "dag", "week", "4 weken", "kwartaal", "jaar", "alle"]
        print(', '.join(periodList))
        payPeriod = input("Kies de gewenste minimum loon berekening: ")
        if not Validation.validateList(payPeriod):
            continue
        else:
            period = payPeriod
            break

    while True:
        fulltimeList = [36, 38, 40]
        print(', '.join(fulltimeList))
        hoursInput = input("Kies een fulltime werkweek in uw branche of sector uit de lijst hierboven: ")
        if not Validation.validateList(hoursInput):
            continue
        else:
            hours = hoursInput
            break

    while True:
        hoursWeekInput = input("Aantal uur dat u per week werkt: ")
        if not Validation.validateWorkingHoursWeek(hoursWeekInput):
            continue
        else:
            hoursWeek = hoursWeekInput
            break

    # # check if the input from user is valid
    # if validateYear(yearInput) and validateSalary(salaryInput) and validateBirthday(birthdayInput):
    #     print("Valid Input")
    # else:
    #     print("Invalid Input")
