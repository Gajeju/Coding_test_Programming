s = input().upper()
alph_list = []

for i in range(65,91):
    alph_list.append(s.count(chr(i)))

answer = max(alph_list)

if alph_list.count(answer) > 1:
    print('?')
else:
    print(chr(alph_list.index(answer) + 65))

# 가장 많이 사용된 알파벳 출력 (입력은 대소문자 구분 x 출력은 대문자로)

# https://www.acmicpc.net/problem/1157