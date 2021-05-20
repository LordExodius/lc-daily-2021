# Oscar Yu
# May 19th, 2021

def letterCasePermutation(self, s: str) -> list[str]:
    letterIndex = [index for index in range(len(s)) if s[index].isalpha()]
    numLetters = len(letterIndex)

    if len(letterIndex) == 0:
        return [s]

    numPerms = (2 ** numLetters)
    permutations = [bin(i)[2:].zfill(numLetters) for i in range(numPerms)]

    result = []

    for perm in permutations:
        permList = [letter for letter in s]
        for index in range(len(perm)):
            letter = letterIndex[index]
            if perm[index] == "0":
                permList[letter] = permList[letter].lower()
            else:
                permList[letter] = permList[letter].upper()
        result.append("".join(permList))

    return result   


print(letterCasePermutation(0, "a1b2")) 