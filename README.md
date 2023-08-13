# Python Assignment4
The goal of this assignment is to create a program with three code blocks:
 - Questions: allow user to create and edit interview questions, then save questions to a csv file for use in Interview and Main
 - Interview: allow user to create candidates and store answers to active questions by question ID to a csv file for use in Main
 - Main: join the csv file with interview questions with the csv file with interviewee answers and question IDs to create a list of questions and answers
Note: functionality within each code block is limited to the parameters of the assignment.  Just say no to gold plating.

# Questions
The questions module allows the user to add, edit, and "retire" questions, then save them to a csv file for use in Interview and Main.  To add questions, the user inputs a string between constants MIN_LENGTH and MAX_LENGTH and then the question is assigned an ID based on it's position in the question list.  This method for generating IDs means that questions cannot be deleted from the list without destroying link to interview answers, so a third value "Active" is used with a value of "Y" or "N" to activate or retire questions.

![Code to add a new question and assign an ID](https://github.com/AFolmer/PythonAssignment4/assets/132308533/41a7b9e8-fe50-47a2-9343-f9a790bf5704)


# Interview
The interview module allows the user to add new candidates and responses to questions, check to make sure existing candidates have answered all active questions, and then save the candidate answers with question IDs for use in Main.  To add a candidate, the user inputs candidate email address with a preventative control to validate that the string includes an '@' and '.', increasing the odds for a valid email address.  Next, they are prompted to provide answers to all active questions in the csv question list. 

![Add values for each candidate + response to answer list](https://github.com/AFolmer/PythonAssignment4/assets/132308533/8176bb0d-805f-48ef-b524-91f3d80e8b09)

Because questions are activated and retired independently of individual interviews, there is a manually initiated check to ensure that each candidate has responded to each active question.  If a response is missing, the program prompts the user to enter a response.

![Data check to validate that all candidates have responses to active questions](https://github.com/AFolmer/PythonAssignment4/assets/132308533/02c32cb8-48ab-4e4a-a7fe-7d83bd1b8bbe)

## Main
The code in the "Main" file is where Questions and Interview come together to create a relational database. I've broken it out into several steps with print outs along the way so that the user can manually scan to ensure that the final table includes the information they need to see.

Step 1: The final goal of the program is to print a list of responses by question, so the first step is to sort the list of answers by question ID

![Sort by value and print](https://github.com/AFolmer/PythonAssignment4/assets/132308533/6947309d-8144-402c-9bab-5ecd5ff60144)

Step 2: Check for answers associated with retired questions and remove them from the list using pop

![Remove answers to retired questions](https://github.com/AFolmer/PythonAssignment4/assets/132308533/d5bf38a4-f16c-4247-8318-53fc1c2be862)

Step 3: Display the number of invalid answers removed from the list and the new, curated list

![Print list of answers to active questions](https://github.com/AFolmer/PythonAssignment4/assets/132308533/686aa916-3a79-467a-932e-ce7b7efa6498)

Step 4: Finally, create a sub-list of answers to each active question with only the fields Candidate and Response by matching value [1] in the answer list to value [2] in the question list

![Create sublist of candidate responses to each question](https://github.com/AFolmer/PythonAssignment4/assets/132308533/4da57a1a-4f84-4d73-8f57-c0b7d0c55f70)

## Common functions
One of the challenges of this assignment is to build in the right preventative controls to ensure users enter data that can be processed as intended and admin functions to keep the main code blocks focused on content unique to the program.  Functions from CSV reader and tabulate are also used to save and print data.

### Menu choice
This function uses a while loop and try/ except value error followed by if/else to ensure that the user enters an integer between 1 and a parameter with the max value for menu choices.

![Menu choice function limiting input to an integer between min and max values](https://github.com/AFolmer/PythonAssignment4/assets/132308533/590d049b-baa2-475d-9a6c-32775e497c83)

### Y or N
This function uses a while loop and if/else to capture a value of Y or N from the user and format with upper() to answer yes or no questions.
![Function to limit user input to Y or N](https://github.com/AFolmer/PythonAssignment4/assets/132308533/f319b846-d9ab-4888-bf68-3cea00ef2f73)

### CSV reader/ writer
CSV reader and writer used with try/except File Not Found error to either open file with csv values to populate list data or create new list if file not found.  At the end of the program, list data is exported and saved to a CSV file.

![CSV reader to import list or create new list](https://github.com/AFolmer/PythonAssignment4/assets/132308533/bb5c64c5-ec84-4074-a277-f31d22a4933e)

![CSV writer to save list data to csv file](https://github.com/AFolmer/PythonAssignment4/assets/132308533/412b6c3e-c533-4a43-8bab-07d146fe1757)

## List comprehension and Tabulate

All lists in this program are formatted using tabulate to print clean columns with custom headers.  List comprehension is used to create sublists with only the information the user needs to see.  Using list comprehension allows the user to filter on field values and curate which fields within a row to pull into the sublist.  It can also be used to transform data, but that functionality is not needed in this program.

![Create sub-list and print with tabulate](https://github.com/AFolmer/PythonAssignment4/assets/132308533/c84c7223-28fd-4f40-aada-094175696b36)

![Create sub-list with only selected fields](https://github.com/AFolmer/PythonAssignment4/assets/132308533/7d5bcbbd-2729-467d-bd39-a087da10a87d)

