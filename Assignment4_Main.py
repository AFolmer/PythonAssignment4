# Python Basics Assignment 4: Validating Data - Main
# AFolmer
# Created 7/20/2023
# Use the interview questions managed by Assignment4_Questions and interview answers managed by Assignment4_Interview
# to create a formatted view of interview responses by question for all active questions

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


def create_candidate_list(answer_list):
    """Create a list of unique email addresses in answer_list
    :param answer_list: list of candidate responses to questions in question list
    :return candidate_list: list of unique email addresses in answer list"""
    candidate_list = []
    for answer in answer_list:
        if answer[0] not in candidate_list:
            candidate_list.append(answer[0])
    return candidate_list


def create_active_question_list(question_list):
    """Create a list of active questions in question list and enforce that ID (question[0]) is an integer
    :param question_list: list of questions
    :return active_question_list: list of active questions"""
    active_questions = [[int(question[0]), question[1]] for question in question_list if question[2] == "Y"]
    return active_questions


MAX_MENU = 3  # Count of main menu choices
# Use the csv module in Python to try to open file questions.csv and save to question_list[]
try:
    with open('questions.csv', newline='') as file:
        reader = csv.reader(file)
        question_list = list(reader)
        file.close()
# Notify users if question list is not found and exit program
except FileNotFoundError:
    sys.exit("The file questions.csv does not exist.")
# Use the csv module in Python to try to open file answers.csv and save to answer_list[]
try:
    with open('answers.csv', newline='') as file:
        reader = csv.reader(file)
        answer_list = list(reader)
        file.close()
# Notify users if answer list is not found and exit program
except FileNotFoundError:
    sys.exit("The file answers.csv does not exist.")
# Create a list of candidates
candidate_list = create_candidate_list(answer_list)
# Create a list of active questions
active_question_list = create_active_question_list(question_list)
# Remove retired questions from answer list and create new print_list with values from
remove_response = 0
# While loop to manage user choices
while True:
    print("1. Check answer file for deleted questions \n2. Print responses by question "
          "\n3. Save and exit")
    main_menu_choice = menu_choice(MAX_MENU)
    # Code block to remove retired answers from list
    if main_menu_choice == 1:
        print("Remove deleted")
        # Print initial list of answers sorted by candidate email address
        print("Initial answer file")
        list.sort(answer_list, key=lambda answer: answer[0])
        print(tabulate(answer_list, headers=["Candidate", "Question ID", "Response"]))
        # Variable to capture count of answers removed from answer list
        invalid_questions = 0
        # For each answer in the answer list, check that the question ID in answer[1] is in the active question list
        for answer in answer_list:
            in_question_list = False
            answer_index = answer_list.index(answer)
            for question in active_question_list:
                # If the question is active, update in_question_list to True and stop
                if int(answer[1]) == int(question[0]):
                    in_question_list = True
                    break
            # If question status is still false, remove answer from list as question is not valid
            if in_question_list is False:
                answer_list.pop(answer_index)
                invalid_questions += 1
        # Display the count of answers removed from list
        print(f'{invalid_questions} invalid questions removed from list')
        # Print the new list of answers that align to valid questions
        print(tabulate(answer_list, headers=["Candidate", "Question ID", "Response"]))
    # Print sub-lists of answers by question and candidate
    elif main_menu_choice == 2:
        print("Responses by question")
        # For each question in the active question list, print candidate responses with matching question ID
        for question in active_question_list:
            # List of answers filtered by question
            answer_by_question = []
            for answer in answer_list:
                if int(answer[1]) == int(question[0]):
                    answer_by_question.append([answer[0], answer[2]])
            # Sort list by candidate email address
            list.sort(answer_by_question, key=lambda answer: answer[0])
            print(f'\n{question[1]}')
            print(tabulate(answer_by_question, headers=["Candidate", "Response"]))
    # Save updates to answer list and exit program
    elif main_menu_choice == 3:
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
    else:
        print("Invalid menu choice")