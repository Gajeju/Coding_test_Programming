n = int(input())
alphabet = [input() for _ in range(n)]
rank_dict = {}

for alph in alphabet:
    alph_len = len(alph)
    for i in range(alph_len):
        rank_dict[alph[i]] = rank_dict.get(alph[i], 0) + (10 ** (alph_len-i-1)) 

for i in range(9, -1, -1):
    if not rank_dict:
        break

    a = max(rank_dict, key=lambda x:rank_dict[x])
    del rank_dict[a]

    for j in range(len(alphabet)):
        alphabet[j] = alphabet[j].replace(a,str(i))

alphabet = list(map(int, alphabet))
print(sum(alphabet))

# 단어 수학문제
# N개의 단어는 알파벳 대문자로만 이루어져 있다.
# N개 단어의 총합이 최대

# 어려웠음 / 출현한 알파벳의 자리수 합을 딕셔너리 형태로 저장하고
# value기준 취대값을 하나씩 빼면서 9부터 차례로 할당한다

# https://www.acmicpc.net/problem/1339