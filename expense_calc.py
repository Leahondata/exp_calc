from datetime import date
import csv
import os
from operator import itemgetter
import matplotlib.pyplot as plt
import numpy as np


def check_csv(filename):
    with open(filename, mode='a'):
        return
    file.close()


# if list is empty, return false, if list contains something, return true
def empty_csv(filename):
    with open(filename, mode='r') as file:
        csv_data = csv.reader(file)
        data = list(csv_data)
        if not data:
            print('Please enter an expense first!')
            return False
        else:
            return data


def read_csv(filename):
    csv_data = []
    with open(filename, mode='r') as file:
        csv_data = list(csv.reader(file))
        # for lines in csvfile:
    file.close()
    return csv_data


def write_csv(list_data, filename):
    '''
    Explanation: takes user data in list format and saves it 
    to the csv file

    Parameters: 

    list_data: a list of data in format: date, category, cost

    filename: a csv file that the data is saved to

    Returns: nothing
    '''
    with open(filename, 'a') as file:
        csvwriter = csv.writer(file)
        for data in list_data:
            csvwriter.writerow(data)
    file.close()


def get_input():
    '''
    Explanation: generates date for and takes user input 
    for expense type and cost

    Parameter: none

    Returns: a list of lists
    '''
    input_data = []
    while True:
        expense_date = date.today()
        expense_date = expense_date.strftime("%m/%d/%Y")
        expense_type = (input(
            "\nWhat is the expense type? \n(if there are no more expenses to enter, type 'done' instead)"))
        if expense_type == 'done':
            break
        expense_cost = (input("\nHow much was spent?"))

        try:
            expense_cost = float(expense_cost)
        except ValueError:
            print("\nThat is not a number, try again!")
        else:
            input_data.append([expense_date, expense_type, expense_cost])
    return input_data


def summarize(list_data):
    summary_dict = {}
    for data in list_data:
        if data[1] not in summary_dict:
            summary_dict[data[1]] = float(data[2])
        else:
            summary_dict[data[1]] += float(data[2])
    return dict(sorted(summary_dict.items(), key=itemgetter(1), reverse=True))


# test functionality for multiple dates worth of data
def display_plot():
    x = []
    y = []
    title = ''

    csv_data = read_csv(datafile_name)
    for row1, row2 in summarize(csv_data).items():
        x.append(row1)
        y.append(row2)
    title = title + csv_data[-1][0]

    plt.bar(x, y)
    plt.xlabel('Category')
    plt.ylabel('Cost')
    plt.title(title)
    plt.savefig('expense_plot.png')


menu_state = 5

while menu_state != 0:
    datafile_name = "expense_calc.csv"
    # print(read_csv(datafile_name))
    print(f"\n=========[ExpCalc v1.1]==========")
    print("1. Add expense")
    print("2. Display expenses")
    print("3. Summarize spending")
    print("4. Display summary plot")
    print("0. Exit program")

    check_csv(datafile_name)

    menu_state = int(input("Choice: "))
    os.system("clear")
    print("")
    csv_data = empty_csv(datafile_name)
    if (menu_state == 1):
        user_data = get_input()
        write_csv(user_data, datafile_name)
    elif (menu_state == 2):
        if csv_data:
            for item in read_csv(datafile_name):
                print(item)
    elif (menu_state == 3):
        if csv_data:
            for category, cost in summarize(csv_data).items():
                print(category, cost)
    elif (menu_state == 4):
        if csv_data:
            display_plot()


# user_data = get_input()
# write_csv(user_data, datafile_name)
# print(read_csv(datafile_name))0

# datafile_name = "expense_calc.csv"
# csv_data = read_csv(datafile_name)
# print(summarize(csv_data))Steam
