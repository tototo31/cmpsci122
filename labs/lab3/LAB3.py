
#  Option 1: I worked on the homework(lab) assignment alone, using only

def countLetters(letter, text):
    count = 0
    for i in text:
        if i  == letter:
            count += 1
    return count

def studentGrades(gradeList):
    avgs = []
    for i in range(1, len(gradeList)):
        avg = 0
        count = 0
        for x in range(1, len(gradeList[i])):
            avg += gradeList[i][x]
            count += 1
        avg = avg//count
        avgs.append(avg)
    return avgs

#TESTING EXAMPLES (Run your own tests too), REMOVE ALL YOUR TESTING CODE BEFORE SUBMITTING
print(countLetters('a','example with a')) #2
print(countLetters('z','I love zuchini bread')) #1
print(countLetters('s','Mississippi')) #4

grades = [
        # First line is descriptive header. Subsequent lines hold data
        ['Student', 'Quiz 1', 'Quiz 2', 'Quiz 3'],  ## Header
        ['John', 100, 90, 80],
        ['McVay', 88, 99, 111],
        ['Rita', 45, 56, 67],
        ['Ketan', 59, 61, 67],
        ['Saranya', 73, 79, 83],
        ['Min', 89, 97, 101]
]
print(studentGrades(grades)) #[90,99,56,62,78,95]


grades = [
        ['Student', 'Quiz 1', 'Quiz 2'],
        ['John', 100, 90],
        ['McVay', 88, 99],
        ['Min', 89, 97]]
print(studentGrades(grades)) #[95,93,93]
