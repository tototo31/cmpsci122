### HW#5 due 03/21 at 7:59 AM 
# Submission Instructions
#  file name: HW5.py
#  Do NOT change any function name

#### COLLABORATION STATEMENT: 
####


# Function takes a string as a parameter and returns True if the string is a palindrome, False otherwise
def isPalindrome(text):

    if not isinstance(text, str): #input must be a string
        return False
    punc = [".", ",", "?", "'", '"', " "] # keep track of what we dont want to be checking
    text = text.lower() # make the case the same for everythin
    temp = "".join([i for i in text if not i in punc]) # remove all punctuation from the string
    # for i in text:
    #     if not i in punc:
    #         temp += i
    text = temp # set our new text
    # Reversing text
    rev = text[::-1]

    # Checking if both strings are equal or not
    if (text == rev):
        return True
    return False
