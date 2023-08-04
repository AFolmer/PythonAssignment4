# Python Basics Assignment 4: Validating Data - Questions
# AFolmer
# Created 7/20/2023
# Create a list of interview question saved to a csv file and allow user to add new questions or
# modify existing questions


import csv
from tabulate import tabulate


def menu_choice(max_value):
    """Validate that user menu choice is an integer within range of menu options
    :param max_value: the number of menu choices
    :return int_choice: validated menu choice"""
    while True:
        try:
            int_choice = int(input(f"Enter menu choice 1 - {max_value}: "))
        except ValueError:
            print("Choice must be an integer.")
        else:
            if 1 <= int_choice <= max_value:
                break
            else:
                print(f"Choice must be between 1 - {max_value}")
    return int_choice


def question_length(min_length, max_length):
    """Validate that user question meets length requirements and return new question for question_list
    :param min_length: shortest length for questions
    :param max_length: longest length for questions
    :return new_question: question meeting length requirement"""
    while True:
        new_question = str(input("What is the new question? "))
        if min_length <= len(new_question) <= max_length:
            break
        else:
            print(f"Length must be between {min_length} and {max_length} characters long.")
    return new_question


def y_or_n():
    """Validate that user enters string value Y or N
    :return y_or_n_answer: user input of Y or N"""
    while True:
        y_or_n_answer = str(input("Enter Y or N: "))
        y_or_n_answer = y_or_n_answer.upper()
        if y_or_n_answer == "Y" or "N":
            break
        else:
            print("Answer must be Y or N")
    return y_or_n_answer


# Main code block
MAIN_MAX_VALUE = 5  # Count of choices in main menu
MIN_LENGTH = 10  # Minimum character length of questions
MAX_LENGTH = 30 # Maximum character length of questions
# Use the csv module in Python to try to open file questions.csv and save to question_list[]
# If file cannot be opened, create the new list question_list[]
try:
    with open('questions.csv', newline='') as file:
        reader = csv.reader(file)
        question_list = list(reader)
        file.close()
# If question file does not exist, notify user and create a new list
except FileNotFoundError:
    print("Question list doesn't exist or can't be opened.")
    question_list = []
# Loop allowing user to edit, remove, and add questions
while True:
    print("1. Edit questions \n2. Remove questions\n3. Add questions \n4. View questions \n5. Save data and exit")
    main_menu_choice = menu_choice(MAIN_MAX_VALUE)
    if main_menu_choice == 1:
        print("Edit questions.")
        # Check to see if there are questions available to edit
        if len(question_list) == 0:
            print("You have no saved questions.")
        else:
            # Go through the list of active questions and as user to validate as correct or update
            for question in question_list:
                if question[2] == "Y":
                    print(f'Edit {question[1]} ')
                    update = y_or_n()
                    # Call function to check that question meets character length requirements
                    if update == "Y":
                        question[1] = question_length(MIN_LENGTH, MAX_LENGTH)
                        print("Question updated")
    elif main_menu_choice == 2:
        print("Remove questions")
        if len(question_list) == 0:
            print("You have no saved questions.")
        # User input to remove question - using third field "Active Question" vs. removing from list to preserve
        # question IDs to maintain integrity with answer list.
        else:
            for question in question_list:
                if question [2] == "Y":
                    print(f'Remove {question[1]} ')
                    remove = y_or_n()
                    if remove == "Y":
                        print("Are you sure?")
                        remove2 = y_or_n()
                        if remove2 == "Y":
                            question[2] = "N"
    elif main_menu_choice == 3:
        # User inputs a new question
        new_question = question_length(MIN_LENGTH, MAX_LENGTH)
        # Question ID assigned based on list length.  Questions are not deleted, they're soft retired to maintain
        # integrity with answer list
        question_id = len(question_list) + 1
        question_list.append([question_id, new_question, "Y"])
    elif main_menu_choice == 4:
        # Print list of all active questions where questions[2] = Y
        active_questions = [question for question in question_list if question[2] == "Y"]
        print(tabulate(active_questions, headers=["ID", "Question", "Active"]))
    elif main_menu_choice == 5:
        # Use csv module in Python to save question_list to csv file questions.csv
        try:
            with open("questions.csv", "w", newline='') as file:
                csvwriter = csv.writer(file)
                csvwriter.writerows(question_list)
                file.close()
        except:
            print("Error saving question file.")
        # Exit program
        finally:
            break
    else:
        print("Invalid menu choice")