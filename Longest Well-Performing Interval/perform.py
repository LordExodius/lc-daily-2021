# Oscar Yu
# May 21st, 2021
# Works, but is extremely inefficent and TLE's when used for large examples on LC
def longestWPI(self, hours: list[int]) -> int:
    
    # checks for well performing intervals from largest to smallest
    currentInterval = len(hours)

    while currentInterval > 0:
        for startIndex in range(len(hours) - currentInterval + 1):
            interval = hours[startIndex:startIndex + currentInterval]
            #print(f"Index [{startIndex}:{startIndex + currentInterval}] = {interval}")

            # if the interval is a well performing interval, return length
            if sum(i > 8 for i in interval) > len(interval)//2:
                print("Longest Interval:", interval)
                return len(interval)

        currentInterval -= 1
    
    # if no well performing intervals have been found, return 0
    else:
        return 0