### LAB #2 due 01/26 at 11:59 pm 
# Submission Instruction
#  - file name: LAB2.py
#  - Do NOT change any function name
#  - Upload all the functions in a file with the correct file name to Vocareum
#  - Do not include test code outside any function in the upload 

# For all homework and lab assignments, you must write comments that include a collaborations statement: ()
#  - I worked on the homework(lab) assignment alone, using only previous and current course materials. OR
#  - I worked on this homework(lab) with [give the names of the people you worked with] and referred to [cite any texts, web sites, 
#    or other materials not provided as this semester's course materials for CMPSC122].

### Keep in mind that you are allowed to work with other students currently taking CMPSC122. 
### Do give credit though using the collaboration statement. 
### The instructor and the TAs should be treated as course material and need not be listed in the collaboration statement.

def removeString(subStr, mainStr):
	# Write your code here
	start = mainStr.find(subStr)
	mainToList = [x for x in mainStr]
	if start == -1:
		#print("Not Found")
		return mainStr
	else:
		#print("removing from", start, "to", start+len(subStr))
		del mainToList[start:start+len(subStr)]
		return "".join(mainToList)

		
def sumNeg(numList):
	total = 0
	for i in numList:
		if i < 0:
			total += i
	return total



#TESTING EXAMPLES (Run your own tests too)
print(removeString('ello', 'Hello John'))
print(removeString('an', 'I like bananas'))
print(removeString('axel', 'Refrigerator'))
print(sumNeg([1,2,3,4,5]))
print(sumNeg([-5,2,3.5,-4.3,5]))
