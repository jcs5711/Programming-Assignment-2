I for my assignment, i decided to develop a personal fiance tracker with the aim to allow the users to record and manage their expenses. The main function of the program includes adding expenses, veiwing all expenses, calculating the total spending and removing entries. i also implamented file storage so that the data is saved and can be accessed again when the program is restarted.

At the start, i chose to use the "re" library for the input validation and file handeling to save the data whic i based off lecture 8. My program was structured into different files in the hopes of keeping my programs code organised which included a main file an Expense class and a untility file for handling data.

I applied the Object-Oriented Programming from lecture 9 by creating an Expense class. This class stored the name and amount of each expense. I used encapsualtion by makking th amount prviate and contrlling access using @property and setter to ensure value are valid. 

I used regular expression to validate expense names, ensuring that only valid characters are accepted and prevents incorrect data being entered into system

For my file handling i created functions to load and save expenses to a file. This allows data to stay between different runs of the class and helps keeping the main program simple.

Finally, I made some tests using assert statements and exceptiopn handling to chekc for valid and invlaid inputs ensuring the program works correclty and handles error correctly 