import math


def solution(X, Y, colors):
    # write your code in Python 3.6
    if 'R' in colors and 'G' in colors:

        dist_R = [math.sqrt(X[i]**2 + Y[i]**2)
                  for i in range(len(X)) if colors[i] == 'R']
        dist_G = [math.sqrt(X[i]**2 + Y[i]**2)
                  for i in range(len(X)) if colors[i] == 'G']

        if (len(dist_R) == len(dist_G)):
            return (len(dist_R))*2

        dist_R.sort()
        dist_G.sort()

        if (len(dist_R) < len(dist_G)):
            cc, cl = dist_R, dist_G
        else:
            cc, cl = dist_G, dist_R

        if (cc[len(cc)-1] < cl[len(cc)]):
            return len(cc)*2

        for i in range((len(cc)-2), -1, -1):
            if (cc[i] < cl[i+1]) and (cl[i] < cc[i+1]):
                return (i+1)*2

    return 0

# https://app.codility.com/programmers/custom_challenge/jurassic_code2022/


X = [-20000]
Y = [20000]
colors = 'G'
sol = solution(X, Y, colors)
print(sol)
