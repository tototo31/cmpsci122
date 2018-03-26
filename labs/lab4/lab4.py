###LAB #4 due 02/09 at 11:59 pm 
# Submission Instructions
#  file name: LAB4.py
#  Do NOT change any function name
#  Upload all the functions in a file with the correct file name to Vocareum
#  Do not include test code outside any function in the upload
#  Test your code with as many inputs as you feel comfortable 
#  Each function must return the output (Do not use print in your final submission)   
#  Upload to Vocareum as instructed in the “Submitting assignments to Vocareum” file by the due date

#### COLLABORATION STATEMENT: 
    #I WORKED ON THIS ALONE
####

# ENTER YOUR ANSWERS FOR EXERCISE ONE HERE
def answers():

    #Write your answer for a) between the quotes (if multiple values, separate them with commas)
    question_a = "126"

    #Write your answer for b) between the quotes (if multiple values, separate them with commas)
    question_b = "1,3,5,9"

    #Write your answer for c) between the quotes (if multiple values, separate them with commas)
    question_c = "0"


    return question_a, question_b, question_c


## DO NOT MODIFY THE return encMessage LINE
def encrypt(message, key):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    encMessage=""

    for character in message:
        if character.lower() in alphabet:
            index = alphabet.find(character.lower())
            newPosition = (index+key)%26 # use the MOD to find the remainder which will be the shift for numbers > 26
            if character.lower() == character: # check to see if .lower() actually changes the character or not
                newCharacter = alphabet[newPosition]
            else:
                newCharacter = alphabet[newPosition].upper()
            encMessage+=newCharacter
        else:
            encMessage+=character

    return encMessage



def decrypt(message, key): # same as encrypt but instead of adding key to index we subract
    alphabet="abcdefghijklmnopqrstuvwxyz"
    encMessage=""

    for character in message:
        if character.lower() in alphabet:
            index = alphabet.find(character.lower())
            newPosition = (index-key)%26 # the change lies here
            if character.lower() == character: # check to see if .lower() actually changes the character or not
                newCharacter = alphabet[newPosition]
            else:
                newCharacter = alphabet[newPosition].upper()
            encMessage+=newCharacter
        else:
            encMessage+=character

    return encMessage


###TESTING EXAMPLES, Create your own testing examples too, these are just a baseline
#print(encrypt("We are Penn State!!!",6)) 
### OUTPUT: Ck gxk Vktt Yzgzk!!!
#print(decrypt("Ck gxk Vktt Yzgzk!!!",6))
### OUTPUT:We are Penn State!!!
#print(decrypt(encrypt("We are Penn State!!!",6),6))
### OUTPUT:We are Penn State!!!

#print(encrypt("We are Penn State!!!",5))
### OUTPUT:Bj fwj Ujss Xyfyj!!!
#print(decrypt("Bj fwj Ujss Xyfyj!!!",5))
### OUTPUT:We are Penn State!!!
#print(decrypt(encrypt("We are Penn State!!!",5),5))
### OUTPUT:We are Penn State!!!

#print(encrypt("THIS IS A TEST", 99)) #test with shift greater than that of the key

#print(decrypt("OCDN DN V OZNO", 99)) # decrypt test with shift greater than the key

#print(encrypt("THIS IS A SYMBOL TEST !@#$%^&*()12345", 5)) # test to make sure symbols and numbers  dont mess things up

#print(decrypt("YMNX NX F XDRGTQ YJXY !@#$%^&*()12345", 5)) # test decrypt with symbols and numbers
