# Python Assignment4
The goal of this assignment is to create a program with three code blocks:
 - Questions: allow user to create and edit interview questions, then save questions to a csv file for use in Interview and Main
 - Interview: allow user to create candidates and store answers to active questions by question ID to a csv file for use in Main
 - Main: join the csv file with interview questions with the csv file with interviewee answers and question IDs to create a list of questions and answers
Note: functionality within each code block is limited to the parameters of the assignment.  Just say no to gold plating.

# Questions
The questions module allows the user to add, edit, and "retire" questions, then save them to a csv file for use in Interview and Main.  To add questions, the user inputs a string between constants MIN_LENGTH and MAX_LENGTH and then the question is assigned an ID based on it's position in the question list.  This method for generating IDs means that questions cannot be deleted from the list without destroying link to interview answers, so a third value "Active" is used with a value of "Y" or "N" to activate or retire questions.

# Interview
The interview module allows the user to add new candidates and responses to questions, check to make sure existing candidates have answered all active questions, and then save the candidate answers with question IDs for use in Main.  To add a candidate, the user inputs candidate email address with a preventative control to validate that the string includes an '@' and '.', increasing the odds for a valid email address.  Next, they are prompted to provide answers to all active questions in the csv question list. 

![image](https://github.com/AFolmer/PythonAssignment4/assets/132308533/02c32cb8-48ab-4e4a-a7fe-7d83bd1b8bbe)

## Common functions
One of the challenges of this assignment is to build in the right preventative controls to ensure users enter data that can be processed as intended and admin functions to keep the main code blocks focused on content unique to the program.  Functions used are:

### Menu choice
This function uses a while loop and try/ except value error followed by if/else to ensure that the user enters an integer between 1 and a parameter with the max value for menu choices.

![Menu choice function limiting input to an integer between min and max values](https://github.com/AFolmer/PythonAssignment4/assets/132308533/590d049b-baa2-475d-9a6c-32775e497c83)

### Y or N
This function uses a while loop and if/else to capture a value of Y or N from the user and format with upper() to answer yes or no questions.
![Function to limin user input to Y or N](https://github.com/AFolmer/PythonAssignment4/assets/132308533/f319b846-d9ab-4888-bf68-3cea00ef2f73)

### CSV reader/ writer
CSV reader and writer used with try/except File Not Found error to either open file with csv values to populate list data or create new list if file not found.  At the end of the program, list data is exported and saved to a CSV file.

![CSV reader to import list or create new list](https://github.com/AFolmer/PythonAssignment4/assets/132308533/bb5c64c5-ec84-4074-a277-f31d22a4933e)

![CSV writer to save list data to csv file](https://github.com/AFolmer/PythonAssignment4/assets/132308533/412b6c3e-c533-4a43-8bab-07d146fe1757)
