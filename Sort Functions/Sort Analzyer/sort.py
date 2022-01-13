import time


def bubbleSort(anArray):
    for sortingThingy in range(len(anArray) - 1, 0, -1):
        for j in range(sortingThingy):
            if anArray[j] > anArray[j + 1]:
                anArray[j], anArray[j + 1] = anArray[j + 1], anArray[j]


def selectionSort(anArray):
    for firstItem in range(len(anArray) - 1):
        minimum = firstItem
        for secondItem in range(firstItem + 1, len(anArray)):
            if anArray[secondItem] < anArray[minimum]:
                minimum = secondItem
        anArray[firstItem], anArray[minimum] = anArray[minimum], anArray[firstItem]


def insertionSort(anArray):
    for i in range(1, len(anArray)):
        value = anArray[i]
        position = i

        while position > 0 and anArray[position - 1] > value:
            anArray[position] = anArray[position - 1]
            position -= 1
        anArray[position] = value


def loadDataArray(fileName):
    temp = []

    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()
        temp.append(int(line))

    fileref.close()

    return temp


def main():
    startTime = time.time()
    endTime = time.time()

    randomData = loadDataArray("data-files/random-values.txt")
    reversedData = loadDataArray("data-files/reversed-values.txt")
    nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
    fewUniqueData = loadDataArray("data-files/few-unique-values.txt")

    # print(randomData[0:50])
    # print(reversedData[0:50])
    # print(nearlySortedData[0:50])
    # print(fewUniqueData[0:50])

    loop = True
    while loop:
        print('\nMain Menu')

        print('1 : Bubble Sort - Random Array')
        print('2 : Bubble Sort - Reversed Array')
        print('3 : Bubble Sort - Nearly Sorted Array')
        print('4 : Bubble Sort - Few Unique Array')

        print('5 : Selection Sort - Random Array')
        print('6 : Selection Sort - Reversed Array')
        print('7 : Selection Sort - Nearly Sorted Array')
        print('8 : Selection Sort - Few Unique Array')

        print(' 9 : Insertion Sort - Random Array')
        print('10 : Insertion Sort - Reversed Array')
        print('11 : Insertion Sort - Nearly Sorted Array')
        print('12 : Insertion Sort - Few Unique Array')

        print('13 : Exit')

        selection = input("Enter Selection (1 - 13) : ")

        if selection == '1':
            print('\nBubble Sort - Random Array')
            startTime = time.time()
            bubbleSort(randomData)
            endTime = time.time()
            print(f"Bubble Sort Random Data: {endTime - startTime} seconds")
            loop = False

        elif selection == '2':
            print('\nBubble Sort - Reversed Array')
            startTime = time.time()
            bubbleSort(reversedData)
            endTime = time.time()
            print(f"Bubble Sort Reversed Data: {endTime - startTime} seconds")
            loop = False

        elif selection == '3':
            print('\nBubble Sort - Nearly Sorted Array')
            startTime = time.time()
            bubbleSort(nearlySortedData)
            endTime = time.time()
            print(
                f"Bubble Sort Nearly Sorted Array Data: {endTime - startTime} seconds")
            loop = False

        elif selection == '4':
            print('\nBubble Sort - Few Unique Array')
            startTime = time.time()
            bubbleSort(fewUniqueData)
            endTime = time.time()
            print(
                f"Bubble Sort Few Unique Array Data: {endTime - startTime} seconds")
            loop = False

        elif selection == '5':
            print('\nSelection Sort - Random Array')
            startTime = time.time()
            bubbleSort(randomData)
            endTime = time.time()
            print(
                f"Bubble Sort Random Array Data: {endTime - startTime} seconds")
            loop = False

        elif selection == '6':
            print('\nSelection Sort - Reversed Array')
            startTime = time.time()
            bubbleSort(reversedData)
            endTime = time.time()
            print(
                f"Bubble Sort Reversed Array Data: {endTime - startTime} seconds")
            loop = False

        elif selection == '7':
            print('\nSelection Sort - Nearly Sorted Array')
            startTime = time.time()
            bubbleSort(nearlySortedData)
            endTime = time.time()
            print(
                f"Bubble Sort Nearly Sorted Array Data: {endTime - startTime} seconds")
            loop = False

        elif selection == '8':
            print('\nSelection Sort - Few Unique Array')
            startTime = time.time()
            bubbleSort(fewUniqueData)
            endTime = time.time()
            print(
                f"Bubble Sort Few Unique Array Data: {endTime - startTime} seconds")
            loop = False

        elif selection == '9':
            print('\nSelection Sort - Random Array')
            startTime = time.time()
            bubbleSort(randomData)
            endTime = time.time()
            print(
                f"Bubble Sort Few Random Array Data: {endTime - startTime} seconds")
            loop = False

        elif selection == '10':
            print('\nSelection Sort - Reversed Array')
            startTime = time.time()
            bubbleSort(reversedData)
            endTime = time.time()
            print(
                f"Bubble Sort Few Reversed Array Data: {endTime - startTime} seconds")
            loop = False

        elif selection == '11':
            print('\nSelection Sort - Nearly Sorted Array')
            startTime = time.time()
            bubbleSort(nearlySortedData)
            endTime = time.time()
            print(
                f"Bubble Sort Few Nearly Sorted Array Data: {endTime - startTime} seconds")
            loop = False

        elif selection == '12':
            print('\nSelection Sort - Few Unique Array')
            startTime = time.time()
            bubbleSort(fewUniqueData)
            endTime = time.time()
            print(
                f"Bubble Sort Few Unique Array Data: {endTime - startTime} seconds")
            loop = False

        elif selection == '13':
            print('Exit')
            loop = False


main()
