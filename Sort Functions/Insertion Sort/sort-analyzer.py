def insertionSort(anArray):
    for i in range(1, len(anArray)):
        value = anArray[i]
        position = i
        
        while position > 0 and anArray[position - 1] > value:
            anArray[position] = anArray[position - 1]
            position -= 1
        anArray[position] = value


nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog", "at", "good", "eye", "cat", "ball", "fish"]

insertionSort(nums)
insertionSort(words)

print(nums)
print(words)
