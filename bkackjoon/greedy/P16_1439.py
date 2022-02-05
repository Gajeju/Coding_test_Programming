s = input()

count_z = 0
count_o = 0

for i in range(len(s)):
    if s[i] == '1' and (i == len(s)-1 or s[i+1] == '0'):
        count_z += 1
    if s[i] == '0' and (i == len(s)-1 or s[i+1] == '1'):
        count_o += 1


print(count_z if count_z < count_o else count_o)







# 0과 1로 이루어진 문자열 S
# 숫자 같게 만들기
# 최소 숫자 구하기

# 시도 1 모두 0 1로 각각 만들어보고 낮은 숫자 리턴

# https://www.acmicpc.net/problem/1439
