exams = []

for x in range(4):
	exams.append(int(input("Enter value for exam %d: " % x+1)))
sum = 0
for x in exams:
	sum += x
average = sum/len(exams)

print("Your average is:", average)
