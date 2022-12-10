def solution(word, prefix="", pos=0, count_max=-1, long=0,
             ultima_letra='', num_transiciones=0):
    # print(f"*** Pref {prefix}, pos {pos}, count_max = {count_max} ", end='')
    # print(f"long = {long}, ult_l = {ultima_letra} , T: {num_transiciones}")
    if pos == len(word):
        return long
    else:
        # Word_1: the same
        num = solution(word, prefix, pos + 1, count_max,
                       long, ultima_letra, num_transiciones)

        if num > count_max:
            count_max = num

        # Word_2: add letter
        if prefix == "":
            long += 1
            ultima_letra = word[pos]
            num_transiciones = 0
        else:
            if word[pos] == prefix[-1]:
                long += 1
                # ultima_letra
                # num_transiciones
            else:
                long += 1
                ultima_letra = word[pos]
                num_transiciones += 1

        if num_transiciones < 3:
            num = solution(
                word, prefix + word[pos], pos + 1,
                count_max, long, ultima_letra, num_transiciones)
            if num > count_max:
                count_max = num

        return count_max


Test_examples = [['aabacbba', 6], ['aabxbaba', 6],
                 ['xxxyxxyyyxyyy', 11], ['atheaxbtheb', 5],
                 ['aaaaabaaaa', 10], ['qwqertyiuiqoipa', 6],
                 ['yyyxxxyxxyyyxyyy', 14], ['abcabcabcabc', 6],
                 ['abcabcabcabca', 6], ['yyyxbzzzxbyyyxbzzzyybyyyxbzzz', 15],
                 ['dadadbdacacacbc', 9]]

word = 'yyyxbzzzxbyyyxbzzzyybyyyxbzzz'
result = solution(word)
print(result)
