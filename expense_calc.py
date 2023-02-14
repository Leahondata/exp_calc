from datetime import date
import matplotlib.pyplot as plt
import numpy as np
import sys
import csv
import os

VERSION = '1.2'


# Reads the data in the CSV file and returns it in a list of lists format.
def read_csv(filename):
    ''' (str) -> lst of lst

    This function opens the CSV file and reads it, line by line, into a list of lists stored in csv_data. 

    Parameters:
    filename (str): The name of the CSV file to be read.

    Returns:
    list of lists: A list of lists representing the data in the file where each inner list is a row in the file.
    '''
    csv_data = []
    with open(filename, mode='r') as file:
        csv_data = list(csv.reader(file))
    return csv_data


# Writes the user's input data to the CSV file.
def write_csv(list_data, filename):
    ''' (lst, str) -> None

    Takes user data in list format and appends it to the CSV file.

    Parameters: 
    list_data (lst): a list of data in the format of: date, category, cost.
    filename (str): The name of the CSV file that the data is written to.

    Returns:
    None.
    '''
    with open(filename, 'a') as file:
        csvwriter = csv.writer(file)
        for data in list_data:
            csvwriter.writerow(data)


# Creates the CSV file for the user's data, or;
# Appends the user's input data to the CSV file that already exists.
def validate_csv(filename):
    ''' (str) -> lst of lst

    This function checks if a CSV file exists, if not it creates it. If the file does exist, it opens the file and reads it.

    Parameters:
    filename (str): The name of the CSV file to be checked.

    Returns:
    False if the file is empty.
    list of lists: if the file is not empty, a list of lists representing the data in the file where each inner list is a row in the file.

    '''
    with open(filename, mode='a'):
        pass
    with open(filename, mode='r') as file:
        data = list(csv.reader(file))
        if not data:
            print('No data yet, please enter at least one expense')
            return False
        else:
            return data


# Asks the user for expense type and cost.
def get_input():
    ''' (input) -> lst of lst

    Generates date for, and takes user input for expense type and cost using text prompts. It makes sure that the cost input by the user is a number.
    It saves these three data inputs in the CSV file, each new input expense on a new line.

    Parameters:
    None.

    Returns: 
    list of lists: A list of lists representing the data in the file where each inner list is a row in the file.
    '''
    input_data = []
    while True:
        expense_date = date.today().strftime("%m/%d/%Y")
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


# Summarizes the data in the CSV file and shows the user by creating a dictionary.
def summarize(list_data):
    ''' (lst of lst) -> dict

    Summarizes the data contained within the CSV file by creating a dictionary.

    Parameters:
    list_data (lst of lst): A list of lists representing the data in the file where each inner list is a row in the file.

    Returns:
    dict: A dictionary where the data in the CSV file is used as key:value pairs without the date, and sorted from largest to smallest.
    '''
    summary_dict = {}
    for data in list_data:
        if data[1] not in summary_dict:
            summary_dict[data[1]] = float(data[2])
        else:
            summary_dict[data[1]] += float(data[2])
    return dict(sorted(summary_dict.items(), key=lambda x: x[1], reverse=True))


# Displays the data from the CSV file in a visual manner.
def display_plot():
    '''
    Displays the summarized data in a visual manner to the user, saved in PNG file.

    Parameters:
    None.

    Returns:
    None.
    '''
    x = []
    y = []
    title = ''

    csv_data = read_csv(expensetracker_datafile_name)
    for row1, row2 in summarize(csv_data).items():
        x.append(row1)
        y.append(row2)
    title = title + csv_data[-1][0]

    plt.bar(x, y)
    plt.xlabel('Category')
    plt.ylabel('Cost')
    plt.title(title)
    plt.savefig('expense_plot.png')
    plt.cla()


# Running the program, using the combined previous functions:
menu_state = 5
while menu_state != 0:
    expensetracker_datafile_name = "expenses_tracked.csv"
    print(
        f"\n=========[ExpTracker v{VERSION}]==========",
        "\n1. Add expense",
        "\n2. Display expenses",
        "\n3. Summarize spending",
        "\n4. Display summary plot",
        "\n0. Exit program"
    )

    # Checks if file has been created, or makes one.
    validate_csv(expensetracker_datafile_name)

    # Asks the user to input a menu selection, and checks for integer format.
    menu_state = (input("Choice [0-4]: "))
    os.system("clear")
    try:
        menu_state = int(menu_state)
    except ValueError:
        os.system("clear")
        print("\nInput must be a value from 0 to 4")

    # Assigned the file check function to a variable named csv_data.
    csv_data = validate_csv(expensetracker_datafile_name)

    # Asks the user to input expense and cost data.
    if (menu_state == 1):
        user_data = get_input()
        write_csv(user_data, expensetracker_datafile_name)
        os.system("clear")

    # Displays the data stored in the CSV file for the user.
    elif (menu_state == 2):
        if csv_data:
            for item in read_csv(expensetracker_datafile_name):
                print(item)

    # Summarizes the data stored in the CSV file for the user.
    elif (menu_state == 3):
        if csv_data:
            for category, cost in summarize(csv_data).items():
                print(category, cost)

    # Displays the summary data from the CSV file in a visual format for the user.
    elif (menu_state == 4):
        if csv_data:
            display_plot()
            print("Plot image has been saved as expense_plot.png")
