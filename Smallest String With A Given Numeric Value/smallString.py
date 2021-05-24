# Oscar Yu
# May 21st, 2021
# getSmallestString2() is a more optimized version using f string formatting

def getSmallestString(self, n: int, k: int) -> str:
    string = [1 for i in range(n)]
    index = n - 1
    k -= n
    while k > 0:
        if string[index] < 26:
            string[index] += 1
            k -= 1  
        else:
            index -= 1
    return "".join([chr(n + 96) for n in string])

def getSmallestString2(self, n: int, k: int) -> str:
    k -= n
    string = ""
    while k > 0:
        if len(string) < n:
            k += 1
        currentLetter = min(k, 26)
        k -= currentLetter
        string = f"{currentLetter + 96:c}" + string
    return f"{string:a>{n}}"

def getSmallestString3(self, n: int, k: int) -> str:
    k -= n
    string = chr((k + k//25)%26 + 97) + k//25 * "z"
    while len(string) > n:
        string = string[1:]
    return f"{string:a>{n}}"

print("\nTEST 1")
print("Solution2:",getSmallestString2(0, 5, 73))
print("Solution3:",getSmallestString3(0, 5, 73))
print("\nTEST 2")
print("Solution2:",getSmallestString2(0, 3, 27))
print("Solution3:",getSmallestString3(0, 3, 27))
print("\nTEST 3")
print("Solution2:",getSmallestString2(0, 5, 130))
print("Solution3:",getSmallestString3(0, 5, 130))
print("\nTEST 4")
print("Solution2:",getSmallestString2(0, 24, 552))
print("Solution3:",getSmallestString3(0, 24, 552))
print("\nTEST 5")
print("Solution2:",getSmallestString2(0, 90, 1191))
print("Solution3:",getSmallestString3(0, 90, 1191))

"aadzzzzzzzzzzzzzzzzzzzzz"
"aaaczzzzzzzzzzzzzzzzzzzz"