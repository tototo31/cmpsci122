
def linearSearch(item, dataList):
    for i in dataList:
        if i == item:
            return True
    return False

def binarySearch(item, dataList):
    #this dataList must be sorted
    if len(dataList) == 0:
        return False
    else:
        midpoint = len(dataList)//2
        if dataList[midpoint] == item:
            return True
        else:
            if dataList[midpoint] > item:
                return binarySearch(item, dataList[:midpoint])
            else:
                return binarySearch(item, dataList[midpoint+1:])

def insertionSort(dataList):
    for index in range(len(dataList)):
        current = dataList[index]
        position = index

        while position > 0 and dataList[position-1] > current:
            dataList[position] = dataList[position-1]
            position -= 1
        dataList[position] = current

    return dataList

# QUICKSORT
def quickSort(dataList):
    quickSortHelper(dataList, 0, len(dataList)-1)
    return dataList

def quickSortHelper(dataList, start, end):
    if start < end:
        split = partition(dataList, start, end)
        quickSortHelper(dataList, start, split-1)
        quickSortHelper(dataList, split+1, end)

def partition(dataList, first, last):
    pivot = dataList[last]
    right = last-1
    left = first
    done = False

    while not done:
        while dataList[left] <= pivot and left <= right:
            left += 1

        while dataList[right] >= pivot and right >= left:
            right -= 1

        if right < left:
            done = True
        else:
            dataList[right], dataList[left] = dataList[left], dataList[right]

    dataList[last], dataList[left] = dataList[left], dataList[last]
    return left
# END QUICKSORT
