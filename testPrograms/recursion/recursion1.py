
def listsum(numbers): # an interative version
    total = 0
    for item in numbers:
        total += item
    return total

def listSumRec(list_num):
    if len(list_num) == 1:
        return list_num[0]
    else:
        return list_num[0] + listSumRec(list_num[1:])


def factorial(n):
    total = 1
    for i in range(2, n+1):
        total *= total
    return total

def factorialRec(n):
    if n == 1:
        return 1
    else:
        return n * factorialRec(n-1)
# some times a recursive function isnt always faster
# this is because you may be recomputing values often
# fibonacciRec(5) will compute fibonacciRec(1) 5 seperate times
def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
    return x

def fibonacciRec(n):
    if n <= 1:
        return n
    else:
        return fibonacciRec(n-1) + fibonacciRec(n-2)
# this is much more optimized than the previous example
# this is because we are saving all the values we compute and never recompute... after huge numbers we might run out of memory
computed = {0:0, 1:1}
def fib(n):
    if not n in computed:
        computed[n] = fib(n-1) + fib(n-2)
    return computed[n]

def reverse_list(lst):
    if len(lst) == 1:
        return lst
    else:
        return reverse_list(lst[1:]) + [lst[0]]
