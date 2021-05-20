# Oscar Yu
# May 18th, 2021
# DOES NOT WORK

def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
    numArrays = -(-len(arr)//k)
    print("Num arrays:", numArrays)
    print(arr)
    
    largest = 0

    # create initial indices for subarrays
    arrayIndices = [i * (k) for i in range(numArrays)]
    print("Indicies:", arrayIndices)
    for i in range(len(arrayIndices)):
            arrayIndices[i] -= 1
    
    # iterates through possible subarray combinations
    for iteration in range(k):
        testArr = [i for i in arr]
        for i in range(len(arrayIndices)):
            arrayIndices[i] += 1
            if arrayIndices[i] > (len(testArr) - 1):
                print("removing", arrayIndices[i])
                #arrayIndices.insert(0, arrayIndices.pop(i) - len(testArr))
                arrayIndices.pop(i)

        print("Indicies:", arrayIndices)
        # loop from 0 to first subarray index
        #print("First subarray start")
        for subIndex in range(arrayIndices[0]):
            print("Maximum of", testArr[:arrayIndices[0]], "is", max(testArr[:arrayIndices[0]]))
            testArr[subIndex] = max(testArr[:arrayIndices[0]])

        # loop through the subarrays
        #print("Inner subarray start")
        for index in range(1, len(arrayIndices)):
            prevIndex = arrayIndices[index-1]
            currentIndex = arrayIndices[index]
            #print(f"begin @ {prevIndex}, end @ {currentIndex}")

            # sets all numbers in subarray to largest # in subarray
            print("Maximum of", testArr[prevIndex:currentIndex], "is", max(testArr[prevIndex:currentIndex]))
            for subIndex in range(prevIndex, currentIndex):
                #print("Assigning", testArr[j], "to", max(testArr[prevIndex:currentIndex]))
                testArr[subIndex] = max(testArr[prevIndex:currentIndex])

        # loop through last subarray index til end
        #print("Last subarray start")
        print("Maximum of", testArr[currentIndex:], "is", max(testArr[currentIndex:]))
        for subIndex in range(currentIndex, len(testArr)):
            testArr[subIndex] = max(testArr[currentIndex:])

        if sum(testArr) > largest:
            largest = sum(testArr)
        print(testArr)
        print("Sum:", sum(testArr))

    return largest

"""
example = [1,4,1,5,7,3,6,1,9,9,3]
k = 4
print("Largest sum:", maxSumAfterPartitioning(0, example, k))
"""