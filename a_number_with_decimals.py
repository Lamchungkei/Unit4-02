# Created by: Kay Lin 
# Created on: 1st-Nov-2017
# Created for: ICS3U
# This program displays rounding number and its decimal places

def dessimals (number_to_round, number_of_decimal_places):

    answer = (number * 10 ** round)
    answer = int (answer + 0.5)
    total_answer = float(answer / 10 ** round)
    print(total_answer)

number = input('Enter number to round off: ')
round = input('Enter number of decimal places: ')
dessimals(number, round)
