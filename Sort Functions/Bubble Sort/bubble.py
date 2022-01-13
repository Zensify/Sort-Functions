def bubbleSort(anArray):
    for sortingThingy in range(len(anArray) - 1, 0, -1):
        for j in range(sortingThingy):
            if anArray[j] > anArray[j + 1]:
                anArray[j], anArray[j + 1] = anArray[j + 1], anArray[j]
 
 
nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog", "at", "good", "eye", "cat", "ball", "fish"]
 
bubbleSort(nums)
bubbleSort(words)
 
print(nums)
print(words)