# 성적이 낮은 순으로 학생 출력하기
# N명의 학생
# 이름과 성적으로 구분
# 성적이 낮은 순서대로 학생의 이름 출력
# 1 <= N <= 100000

n = int(input())
lst = [list(input().split()) for _ in range(n)]
lst.sort(key = lambda x:int(x[1]))

for i in lst:
    print(i[0], end=' ')