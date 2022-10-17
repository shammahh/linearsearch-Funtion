


nums = [10, 30, 40, 45, 70, 80, 85, 90, 100]
words = ["at", "ball", "cat", "dog", "eye", "fish", "good"]
unsorted = [30, 20, 70, 40, 50, 100, 90]

def linear(arr, element):
    counter = 0
    for i in range(len(arr)):
        if arr[i] != element:
            counter += 1
        if arr[i] == element:
            return element, counter
        if counter == len(arr):
            return element, -1

print(linear(nums, 100))     ## (100, 8)
print(linear(nums, 75))      ## (75, -1)
print(linear(words, "fish")) ## ('fish', 5)
print(linear(words, "at"))   ## ('at', 0)
print(linear(unsorted, 70))  ## (70, 2)
