def is_han(a: int) -> bool:
    n_list = list(map(int, str(a)))
    if len(n_list) == 1:
        return True

    diff = n_list[1] - n_list[0]

    for i in range(1, len(n_list) -1):
        last_diff = diff
        diff = n_list[i+1] - n_list[i]
        if last_diff != diff:
            return False
    return True
 
n = int(input())
cnt = 0
for i in range(1, n+1):
    if is_han(i):
        cnt += 1

print(cnt)


# 양의 정수 X 각 자리수가 등차수열을 이루면 한수

# https://www.acmicpc.net/problem/1065