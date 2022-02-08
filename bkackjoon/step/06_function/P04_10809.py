s = input()

for c in range(97, 123):
    try:
        print(f'{s.index(chr(c))}', end=' ')
    except:
        print('-1',end=' ')


# 알파벳 소문자로만 이루어진 s
# 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 ㄱㅇ우에는 -1출력


# https://www.acmicpc.net/problem/10809