#ex 1
animals = [{"name": "dog", "size": "medium", "age": 3}, {"name": "lion", "size": "big", "age": 12}, {"name": "snake", "size": "small", "weight": 1}]

animal_names = map(lambda x: x["name"], animals)
print(list(animal_names))


#ex 2
numList = [1,2,3,4,5]

doubled_odds = map(lambda x: x*2, filter(lambda n: n % 2, numList))
print(doubled_odds)

# or
doubled_odds = [n *2 for n in numList if n%2 ==1]

#ex 3
numList = [1,2,3,4,5]
by3 = map(lambda x: x*3)
print(by3)

# or

by3 = [x*3 for x in numList]
print(by3)


#ex 4
text = "My lucky number is 45, but I list 25 better"
#create  list of all numbers
numbers = [x for x in text if x.isdigit()]
print(numbers)

#ex 5

def farenheit(T):
    return (9/5)*T + 32
