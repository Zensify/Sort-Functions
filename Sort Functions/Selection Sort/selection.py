import time


def selectionSort(anArray):
    TimeStart = time.perf_counter()
    for firstItem in range(len(anArray) - 1):
        minimum = firstItem
        for secondItem in range(firstItem + 1, len(anArray)):
            if anArray[secondItem] < anArray[minimum]:
                minimum = secondItem
        anArray[firstItem], anArray[minimum] = anArray[minimum], anArray[firstItem]
        TimeEnd = time.perf_counter()
        TimeOutput = TimeEnd - TimeStart
        print(f"{TimeOutput}")

nums = [10, 30, 40, 45, 70, 80, 85, 90, 100]
words = ["at", "ball", "cat", "dog", "eye", "fish", "good"]

selectionSort(nums)
selectionSort(words)

print(nums)
print(words)
