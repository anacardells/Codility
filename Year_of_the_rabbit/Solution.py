# https://app.codility.com/programmers/challenges/year_of_the_rabbit_2023/

def solution(A, B):
    N = len(A)
    Index_B = list(range(N))

    for pos in range(N):
        Found = True
        for i in range(N):
            if A[i] == B[Index_B[i]]:
                Found = False
                break
        if Found:
            return (pos)
        Index_B = [Index_B[-1]] + Index_B[:-1]
    return (-1)


TestCases = [[[1, 3, 5, 2, 8, 7], [7, 1, 9, 8, 5, 7], 2],
             [[1, 1, 1, 1], [1, 2, 3, 4], -1],
             [[3, 5, 0, 2, 4], [1, 3, 10, 6, 7], 0]]

for test in TestCases:
    result = solution(test[0], test[1])
    expected = test[2]

    if result == expected:
        print("OK!")
        pass
    else:
        print("ERROR! (expected: " + str(expected) + ")" +
              " (result: " + str(result) + ")")
