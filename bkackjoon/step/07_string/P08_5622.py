dic = {'ABC':3, 'DEF':4, 'GHI':5, 'JKL':6, 'MNO':7, 'PQRS':8, 'TUV':9, 'WXYZ':10}
sec = 0

s = input()

for c in s:
    for key in dic.keys():
        if c in key:
           sec += dic[key]

print(sec)


# https://www.acmicpc.net/problem/5622