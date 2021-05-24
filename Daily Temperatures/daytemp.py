# Oscar Yu
# May 22nd, 2021

# stuck on test case 29
def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
    nextHigh = []
    for tempIndex in range(len(temperatures)):
        currentTemp = temperatures[tempIndex]
        for nextIndex in range(tempIndex, len(temperatures)):
            if temperatures[nextIndex] > currentTemp:
                nextHigh.append(nextIndex - tempIndex)
                break
        else:
            nextHigh.append(0)
    return nextHigh

temps = [73, 74, 75, 71, 69, 72, 76, 73]

print(dailyTemperatures(0, temps))

# this one is worse than number 1
# stuck on test case 28
def dailyTemperatures2(self, temperatures: list[int]) -> list[int]:
    nextHigh  = []
    for ind, temp in enumerate(temperatures):
        try:
            nextHigh.append(next(index for index, value in enumerate(temperatures[ind:]) if value > temp))
            print(f"next temp higher than {temp} is {nextHigh[ind]}")
        except:
            print(f"could not find temp higher than {temp}")
            nextHigh.append(0)
    return nextHigh

print(dailyTemperatures2(0, temps))