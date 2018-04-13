from math import sqrt
squares = map(lambda x,y: x*y, [0,1,2,3,4,5], [1,2,3,4,5,6])
print(list(squares))

x = map(sqrt, [1,4,9,16])
print(list(x))

a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]

print(list(map(lambda x,y: x+y, a, b)))
print(list(map(lambda x,y,z: x+y+z, a, b, c)))
print(list(map(lambda x,y,z: 2.5*x + 2*y - z, a, b, c)))


fib = [0,1,1,2,3,5,8,13,21,34,55]
num1 = filter(lambda x: x % 2, fib)
print(list(num1))
num2 = filter(lambda x: x%2 == 0, fib)
print(list(num2))

from functools import reduce
x = reduce(lambda a,b: a if (a>b) else b, [48,12,43,103,14])
print(x)


factorial = reduce(lambda x, y: x*y, range(1,49))
print(list(factorial))

