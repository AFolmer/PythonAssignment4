# Python Basics Assignment 4: Validating Data - Interview
# AFolmer
# Created 7/20/2023
# Use the questions managed in Assignment4 questions to collect and store answers in a csv file


import csv
import sys

from tabulate import tabulate


def menu_choice(max_value):
    """Validate that user menu choice is an integer within range
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


def validate_email(answer):
    """Validates that answer contains '@' and '.'
    :param answer: answer to question what is your email address
    :return email: validated to contain '@' and '.'"""
    while True:
        if "@" and "." in answer:
            email = answer
            break
        else:
            print("Missing @ or '.'")
            answer = input("Enter e-mail address: ")
    return email


def create_active_question_list(question_list):
    """Create a list of active questions in question list and enforce that ID (question[0]) is an integer
    :param question_list: list of questions
    :return active_question_list: list of active questions"""
    active_questions = [[int(question[0]), question[1]] for question in question_list if question[2] == "Y"]
    return active_questions


def create_candidate_list(answer_list):
    """Create a list of unique email addresses in answer_list
    :param answer_list: list of candidate responses to questions in question list
    :return candidate_list: list of unique email addresses in answer list"""
    candidate_list = []
    for answer in answer_list:
        if answer[0] not in candidate_list:
            candidate_list.append(answer[0])
    return candidate_list


def candidate_answers(email, answer_list):
    """Create a list of answers for specified candidate
    :param email: candidate email address used as key in answer list
    :param answer_list: list of all candidate responses
    :return candidate_answer_list: answers for only the specified candidate"""
    candidate_answer_list = []
    for answer in answer_list:
        if answer[0] == email:
            # Enforcing that the ID in answer[1] is an integer to enable comparing lists to lists
            candidate_answer_list.append([answer[0], int(answer[1]), answer[2]])
    return candidate_answer_list


MAX_MENU = 4
# Use the csv module in Python to try to open file questions.csv and save to question_list[]
try:
    with open('questions.csv', newline='') as file:
        reader = csv.reader(file)
        question_list = list(reader)
        file.close()
# Notify users if question list is not opened and exit program
except FileNotFoundError:
    sys.exit("No questions available to conduct interview")
# Use the csv module in Python to try to open file answers.csv and save to answer_list[]
try:
    with open('answers.csv', newline='') as file:
        reader = csv.reader(file)
        answer_list = list(reader)
        file.close()
# Notify users if question list is not opened and creates answer_list[]
except FileNotFoundError:
    print("Answer list doesn't exist or can't be opened.")
    answer_list = []
# Create a curated question list of only active questions
active_questions = create_active_question_list(question_list)
if len(active_questions) == 0:
    sys.exit("No active questions available for interview")
# While loop to manage interview responses
while True:
    print("1. Enter new interview responses \n2. Validate existing interview responses \n3. View all responses"
          "\n4. Save and exit")
    main_menu_choice = menu_choice(MAX_MENU)
    # Enter responses for a new candidate
    if main_menu_choice == 1:
        # Input candidate email address and validate that it contains @ and '.'
        answer = input("What is candidate's email address? ")
        email = validate_email(answer)
        # Create an answer_list sub-list of unique email addresses
        candidate_list = create_candidate_list(answer_list)
        # If candidate email already used, notify user else capture answers for all active questions
        if email in candidate_list:
            print("Candidate responses already captured.")
        # Append an answer for each active question in active question list
        else:
            for question in active_questions:
                answer = input(f'{question[1]} ')
                # Enforcing that ID is an integer to enable comparing lists against lists
                answer_id = int(question[0])
                answer_list.append([email, answer_id, answer])
    elif main_menu_choice == 2:
        # Create an answer_list sub-list of unique email addresses
        candidate_list = create_candidate_list(answer_list)
        # Notify user if there are no candidates
        if len(candidate_list) == 0:
            print("There are no candidate responses to review")
        else:
            # Create a sub-list of responses for each candidate and validate completeness against active questions
            for candidate in candidate_list:
                candidate_answer_list = candidate_answers(candidate, answer_list)
                for question in active_questions:
                    found = False
                    for response in candidate_answer_list:
                        if question[0] == response[1]:
                            found = True
                            break
                    # If question response not found, input response and save to answer list
                    if found is False:
                        print(f'Candidate: {candidate}')
                        new_answer = input(f'{question[1]} ')
                        answer_list.append([candidate, int(question[0]), new_answer])
        print("QA check for missing candidate responses to active questions complete.")
    elif main_menu_choice == 3:
        # Print list of all responses
        print(tabulate(answer_list, headers=["E-mail", "Question ID", "Response"]))
    elif main_menu_choice == 4:
        # Save answers to file and exit program
        try:
            with open("answers.csv", "w", newline='') as file:
                csvwriter = csv.writer(file)
                csvwriter.writerows(answer_list)
                file.close()
        except:
            print("File not saved")
        finally:
            print("Goodbye")
            break

