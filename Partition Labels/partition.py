# Oscar Yu
# May 25th, 2021

def partitionLabels(self, s: str) -> list[int]:
    # had to write getSet method because set() doesn't return in the right order
    def getSet(l):
        setList = []
        for letter in l:
            if not letter in setList:
                setList.append(letter)
        return setList
    
    partitions = []
    setLetters = getSet(s)
    #print(f"Remaining letterSet: {setLetters}")

    while len(setLetters) > 0:
        letter = setLetters[0]
        left = s.find(letter)
        right = s.rfind(letter)

        while any(s.rfind(subLetter) > right for subLetter in getSet(s[left:right])):
            right = max(s.rfind(subLetter) for subLetter in getSet(s[left:right]))
        else:
            #print(f"Left: {left} w/ {s[left]}")
            #print(f"Right: {right} w/ {s[right]}")
            #print(f"subset: {getSet(s[left:right+1])}")
            for subLetter in getSet(s[left:right+1]):
                setLetters.remove(subLetter)
            partitions.append(right - left + 1)
            #print(f"Remaining letterSet: {setLetters}")

    return partitions
    

s = "ababcbacadefegdehijhklij"
s2 = "eccbbbbdec"
print(partitionLabels(0, s))
print()
print(partitionLabels(0, s2))