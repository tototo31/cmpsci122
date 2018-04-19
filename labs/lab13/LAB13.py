### LAB #13 due 04/20 at 11:59 pm 
# Submission Instructions
#  file name: LAB13.py
#  Do NOT change the funtion name, variable names or return values

#### COLLABORATION STATEMENT: 
####

def answers():
	#Each nested list is  of size 11. Enter the values in the corresponding spot.
	#Example: ex1_a=[[11],[1],[],[3],[],[],[],[7],[],[],[10]]

	ex1_a=[[],[12],[],[14],[36],[59],[6],[26],[96],[42],[10]]
	
	ex1_b=[[],[12],[26],[14],[36],[],[6],[59],[96],[42],[10]]
	
	ex1_c=[[],[12],[],[14],[36],[59],[6],[26],[96],[42],[10]]

	return ex1_a,ex1_b,ex1_c

def bubble_sort(numList):
    if len(numList) >= 2:
        sort = False
        while not sort:
            swapped = 0
            for i in range(1,len(numList)):
                if numList[i-1] > numList[i]:
                    numList[i], numList[i-1] = numList[i-1], numList[i] # swap
                    swapped += 1 #increment counted
            if swapped == 0:
                sort = True
            print(numList)
    return numList


# def main():
#     print(bubble_sort([2,3,5,4,1]))

# main()
