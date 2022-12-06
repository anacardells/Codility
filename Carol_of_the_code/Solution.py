def inicialize_dicc(S):
    #######
    # Input: Info os the first tile
    # Output: a dictionary with this structure:
    # the key is the letter that is on the right position
    # (the next color to match)
    # the value is the number of turns we have done so far
    # We keep information of the four posible paths
    #######
    length_paths = {}
    length_paths[S[2]] = 1  # If we position S[0] on the left
    length_paths[S[3]] = 2
    length_paths[S[0]] = 1
    length_paths[S[1]] = 0
    return length_paths


def update_dicc(length_paths, S):
    new_dicc = {}
    new_dicc[S[2]] = length_paths[S[0]] + 1  # If we position S[0] on the left
    new_dicc[S[3]] = length_paths[S[1]] + 2
    new_dicc[S[0]] = length_paths[S[2]] + 1
    new_dicc[S[1]] = length_paths[S[3]] + 0
    return new_dicc


def choose_lesser_turns_path(length_paths):
    sol = length_paths['W']
    for length in length_paths.values():
        if length < sol:
            sol = length
    return sol


def solution(A):
    length_paths = inicialize_dicc(A[0])
    for i in range(1, len(A)):
        length_paths = update_dicc(length_paths, A[i])
    return choose_lesser_turns_path(length_paths)


A = ["RGBW", "GBRW"]
print(solution(A))  # 1
A = ["WBGR", "WBGR", "WRGB", "WRGB", "RBGW"]
print(solution(A))  # 4
A = ["RBGW", "GBRW", "RWGB", "GBRW"]
print(solution(A))  # 2
A = ["GBRW", "RBGW", "BWGR", "BRGW"]
print(solution(A))  # 2
