def reduce_size(P, Q):
    pair_list = []
    P_short = ''
    Q_short = ''
    for i in range(len(P)):
        set_i = set([P[i], Q[i]])
        if set_i not in pair_list:
            pair_list.append(set_i)
            P_short += P[i]
            Q_short += Q[i]
    return P_short, Q_short


def insert_letter(string, letter):
    """
    Inserts a letter in an ordered string using binary search
    """
    low = 0
    high = len(string) - 1
    while low <= high:
        mid = (low + high) // 2
        if letter < string[mid]:
            high = mid - 1
        elif letter > string[mid]:
            low = mid + 1
        else:
            return string[:mid] + letter + string[mid:]
    return string[:low] + letter + string[low:]


def solution(P, Q):
    P, Q = reduce_size(P, Q)
    memo_new = {}
    memo_new[P[0]] = 1
    memo_new[Q[0]] = 1
    for i in range(1, len(P)):
        memo = memo_new
        memo_new = {}
        for key, value in memo.items():
            if (P[i] in key) or (Q[i] in key):
                memo_new[key] = value
            if P[i] not in key:
                key_p = insert_letter(key, P[i])
                memo_new[key_p] = value + 1
            if ((P[i] != Q[i]) and (Q[i] not in key)):
                key_q = insert_letter(key, Q[i])
                memo_new[key_q] = value + 1
    return min(memo_new.values())


TestCases = [
    ['abc', 'bcd', 2],
    ['axxz', 'yzwy', 2],
    ['bacad', 'abada', 1],
    ['amz', 'amz', 3],
    ['dddabc', 'abcefg', 3],
    ['bsqafgiulewghfiaaplskfhjkldsafjhlkafgsdjhluhefdiuahfulidhg',
     'bsdafgiulewghficahlskfhjklzfafjhlkafgsdjwluhefdiurhfueidhg', 14]
]

for test in TestCases:
    result = solution(test[0], test[1])
    expected = test[2]
    if result == expected:
        print("OK!")
        pass
    else:
        print("ERROR! (expected: " + str(expected) + ")" +
              " (result: " + str(result) + ")")

# General info (https://betterprogramming.pub/what-are-frozen-sets-in-python-88f8a15a28dc):
# Sets are an unordered, mutable data type where each value must be unique.
# Frozen sets are a native data type in Python that have the qualities of sets 
#        — including class methods — but are immutable like tuples.
# If you pass a set to the function, it will return the same set, which is now immutable.
# A tuple is a collection which is ordered and unchangeable.

# Older implementations:

# 1) Recursive solution -> Error: Maximum recursion depth exceeded
#
# def update_memo(P, Q, frozen_prefix, value, memo):
#     if P in memo:
#         if Q in memo[P]:
#             memo[P][Q][frozen_prefix] = value
#         else:
#             memo[P][Q] = {}
#             memo[P][Q][frozen_prefix] = value
#     else:
#         memo[P] = {}
#         memo[P][Q] = {}
#         memo[P][Q][frozen_prefix] = value
#     return memo
#
# def solution_recursive(P, Q, prefix=set(), memo={}):
#     frozen_prefix = frozenset(prefix)
#     if P in memo:
#         if Q in memo[P]:
#             if frozen_prefix in memo[P][Q]:
#                 return memo[P][Q][frozen_prefix]
#     if len(P) == 0:
#         return len(prefix)
#     else:
#         # ord('a') = 97
#         prefix_p = prefix.copy()
#         prefix_q = prefix.copy()
#         prefix_p.add(P[0])
#         prefix_q.add(Q[0])
#         opcion_p = solution_recursive(P[1:], Q[1:], prefix_p, memo)
#         opcion_q = solution_recursive(P[1:], Q[1:], prefix_q, memo)
#         memo = update_memo(P, Q, frozen_prefix, min(opcion_p, opcion_q), memo)
#         return memo[P][Q][frozen_prefix]

# 2) Loop + kill equal branches: SILVER AWARD
#
# def initialize_memo(P, Q):
#     memo = {}
#     list_letters = [0] * (ord('z') - ord('a') + 1)
#     key_p = list_letters.copy()
#     key_p[ord(P[0]) - ord('a')] = 1
#     memo[tuple(key_p)] = 1
#     key_q = list_letters.copy()
#     key_q[ord(Q[0]) - ord('a')] = 1
#     memo[tuple(key_q)] = 1
#     return memo
#
# def solution_loop(P, Q):
#     dicc_letras = {chr(i): i - 97 for i in range(97, 123)}
#     memo = initialize_memo(P, Q)
#     for i in range(1, len(P)):
#         memo_new = {}
#         pos_p = dicc_letras[P[i]]
#         pos_q = dicc_letras[Q[i]]
#         for key, value in memo.items():
#             if key[pos_p] == 1:
#                 memo_new[key] = value
#             else:
#                 key_p = list(key)
#                 key_p[pos_p] = 1
#                 memo_new[tuple(key_p)] = value + 1
#             if P[i] != Q[i]:
#                 if key[pos_q] == 1:
#                     if key[pos_p] == 0:
#                         memo_new[key] = value
#                 else:
#                     key_q = list(key)
#                     key_q[pos_q] = 1
#                     memo_new[tuple(key_q)] = value + 1
#         memo = memo_new
#     return min(memo.values())
