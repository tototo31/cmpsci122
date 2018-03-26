### Homework 1 due 01/22(Mon) at 11:59 pm 100 points
#
#   For the non-coding exercises, do the following to write your answers in the answers() funtion
#
#   Step 1: On a sheet of paper (on in your HW1 file), find the answers for the Section 1 questions
#
#   Step 2: For each question, write your answer in the corresponding variable.  
#           Make sure you are submitting your answers in the right variable.
#           For parts b) and c) use T and F (CAPITAL LETTERS) to fill out the list with your answers
#
#
#
#   SUBMISSION:
#       - file name = HW1.py
#       - Do not change any function name
#       - You can test your code with as many inputs as you feel comfortable 
#		- Each funtion must return the output (Do not use print in your final submision)   
#       - Upload to Vocareum as instructed in the “Submitting assignments to Vocareum” file by the due date
#



def answers():

    #Write your answer for a)
    interpreter_output = 0 

    #Write your answer for b), use T for true and F for false (CAPITAL LETTERS)
    expression_eval = ["T","F","F","F"] 
   
    #Write your answer for c), use T for true and F for false (CAPITAL LETTERS)
    truth_table = ["T","T","T","T","T","T","F","T"]
    
 
    return interpreter_output, expression_eval,truth_table
 
def numDigits(number):
#PUT YOUR CODE HERE
#number is an integer
	strin = str(number)
	return len(strin)

def dayName(number):
#PUT YOUR CODE HERE
#number is an integer
	day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
	return day[number]



def countEven(num_list):
#PUT YOUR CODE HERE
#num_list is an list of integers
	count = 0
	for i in num_list:
		if (i % 2 == 0):
			count += 1
	return count

