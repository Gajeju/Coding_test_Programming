n = int(input())
str_list = [input() for _ in range(n)]
cnt = 0

for i in range(n):
    new_str = ''
    last = -1
    for j in range(len(str_list[i])):
        if str_list[i][j] != last:
            if str_list[i][j] in new_str:
                break
            new_str += str_list[i][j]
        last = str_list[i][j]
    else: cnt+=1
    

print(cnt)




# 한 문자에 대하여 연속해서만 나타나는 경우 그룹단어
# 그룹단어의 개수 리턴
# 1. 연속해서 나오는 문자를 하나로 축약하고 각 문자의 개수가 1보다 크면 그룹단어가 아니다

# https://www.acmicpc.net/problem/1316