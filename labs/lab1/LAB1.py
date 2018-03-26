### LAB 1 due at the end of your recitation 
# Goal:
#   Write the three functions asked in the LAB 1 exercises file 

# Submission Instruction
#  - file name: LAB1.py
#  - Do NOT change any function name
#  - Upload all the functions in a file with the correct file name to Vocareum (You can work on Vocareum too)
#  - Do not include test code outside any function in the upload 


def checkNum(number):
    if(number > 0):
        return "Positive"
    elif(number < 0):
        return "Negative"
    else:
        return "0"


def countOdd(num_list):
	#PUT YOUR CODE HERE
	# num_list: list that contains positive integers
    count = 0
    for i in num_list:
        if i % 2 == 1:
            count += 1
    return count

def sum_of_squares(num_list):
	#PUT YOUR CODE HERE
	# num_list: list that contains positive integers
    total = 0
    for i in num_list:
        total += i**2
    return total



