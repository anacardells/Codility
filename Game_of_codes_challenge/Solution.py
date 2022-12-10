# Code inspired by siakhooi

class Block:
    def __init__(self, size, letter):
        self.size = size
        self.letter = letter

    def __str__(self) -> str:
        return f"Block: {self.letter}, {self.size}"


def get_basic_blocks(S):
    allBlock = []
    letters = set()
    currentLetter = ''
    currentBlock = None

    # Collapse trivial blocks
    for i in range(len(S)):
        if S[i] == currentLetter:
            currentBlock.size += 1
        else:
            currentBlock = Block(1, S[i])
            allBlock.append(currentBlock)
            currentLetter = S[i]
            letters.add(currentLetter)

    return allBlock, letters


def solution(S: str) -> int:
    allBlock, letters = get_basic_blocks(S)

    lastBlockLength = {k: [0, 0, 0, 0] for k in letters}
    maxLengthBefore = [0, -1, -1, -1]

    for block in allBlock:
        # print(block)
        # Compute results for j number of blocks
        for j in range(3, -1, -1):

            if maxLengthBefore[j] == -1:
                continue
            currentMax = maxLengthBefore[j]

            # Perform 2 different actions:

            # 1) COMBINE: Consider the possibility of fusing block with the last block of the same character
            #    Result: same number of blocks j ("movement: up")
            if j > 0 and lastBlockLength[block.letter][j] != 0:
                combineLength = lastBlockLength[block.letter][j] + block.size
                maxLengthBefore[j] = max(maxLengthBefore[j], combineLength)
                lastBlockLength[block.letter][j] = combineLength

            # 2) STAY: Consider the possibility of keeping current string and adding the block at the end
            #    Result: one more block j+1 ("movement: up and right")
            if j < 3:
                combineLength = currentMax + block.size
                maxLengthBefore[j + 1] = max(maxLengthBefore[j + 1], combineLength)
                lastBlockLength[block.letter][j + 1] = max(lastBlockLength[block.letter][j + 1], combineLength)

        # print("maxLengthBefore: ", maxLengthBefore)
        # print("lastBlockLength: ", lastBlockLength)

    return max(maxLengthBefore[1], maxLengthBefore[2], maxLengthBefore[3])


# TestCases = [['xxxyxxyyyxyyy', 11]]

TestCases = [['aabacbba', 6],
             ['aabxbaba', 6],
             ['aabxabxba', 6],
             ['xxxyxxyyyxyyy', 11],
             ['atheaxbtheb', 5],
             ['aaaaabaaaa', 10],
             ['qwqertyiuiqoipa', 6],
             ['yyyxxxyxxyyyxyyy', 14],
             ['abcabcabcabc', 6],
             ['abcabcabcabca', 6],
             ['yyyxbzzzxbyyyxbzzzyybyyyxbzzz', 15],
             ['dadadbdacacacbc', 9],
             ['xjojojooojojox', 9],
             ['xjojojooojojo', 9]]

for test in TestCases:
    result = solution(test[0])

    expected = test[1]

    print(test[0] + ' -> ', end='')
    if result == expected:
        print("OK!")
        pass
    else:
        print("ERROR! (expected: " + str(expected) + ")" +
              " (result: " + str(result) + ")")
