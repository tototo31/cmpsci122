### LAB #8 due 03/16 at 11:59 pm 
# Submission Instructions
#  file name: LAB8.py
#  Do NOT change any function name

#### COLLABORATION STATEMENT: 
####

# ENTER YOUR ANSWER FOR EXERCISE ONE HERE
def answers():

    #Write your answer between the quotes 
    ex_1 = "28"

    return ex_1

# DO NOT MODIFY THIS FUNCTION
def triangle(n):
    return recursive_triangle(n, n)

def recursive_triangle(k, n):
    if k > n:
        k = n
    if k < 1 or n <= 0:
        return
    return " "*(n-1)+"*\n" if k == 1 else " "*(n-k)+"*"*k+"\n"+recursive_triangle(k-1, n)
