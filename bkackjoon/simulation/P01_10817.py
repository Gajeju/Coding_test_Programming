# 세 정수가 주어진다. 두 번째로 큰 정수 출력

n_list = list(map(int, input().split()))
n_list.remove(max(n_list))
print(max(n_list))
