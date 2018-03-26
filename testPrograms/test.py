#!/usr/local/bin/python3
import time



def collatz(num,showSteps=False, count=0, steps=[]):
    if num == 0:
        return -1
    if num %2 == 0:
        num = num//2
    else:
        num = num*3+1

    steps.append(num)
    count += 1
    if num == 1 and showSteps:
        print("These are the steps taken", steps)
    return count if num == 1 else collatz(num, showSteps, count, steps)


if __name__ == "__main__":
    num = int(input("Enter a number > 0 or -1 to stop: "))
    while num != -1:
        steps = collatz(num)
        print("It took %d steps to reach 1" % steps)
        num = int(input("Enter a number > 0 or -1 to stop: "))
    maxSteps = [0, 0] # num of max - num of steps taken
    start = time.time()
    rng = int(input("Enter a number for test range or -1 to exit: "))
    while  rng != -1:
        for i in range(1, rng):
            print("Testing %d." % i, end=" ")
            stepsTaken = collatz(i)
            print("Finished in %d steps." % stepsTaken)
            if stepsTaken > maxSteps[1]:
                maxSteps = [i, stepsTaken]
                print("New Max")
        print("Max steps taken in range was %d and was taken by %d." % (maxSteps[1], maxSteps[0]))
        print(" --- Time Taken: %f --- " % (time.time() - start))
        rng = int(input("Enter a number for test range or -1 to exit: "))
