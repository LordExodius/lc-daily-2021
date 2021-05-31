def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
    poisonedTime = 0
    prevEnd = 0
    for attack in timeSeries:
        if attack < prevEnd:
            print("add attack time")
            poisonedTime += attack + duration - prevEnd
        else:
            print("add full duration")
            poisonedTime += duration
        prevEnd = attack + duration
    return poisonedTime

print(findPoisonedDuration(0, [1, 4], 2))
print(findPoisonedDuration(0, [1, 2], 2))