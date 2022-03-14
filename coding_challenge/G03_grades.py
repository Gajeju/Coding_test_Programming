# 학생의 점수를 의미하는 정수 A가 입력될 때 학생의 학점을 출력하는 프로그램을 작성하세요.
# 점수에 따른 출력 내용은 다음과 같습니다.
# 1) 점수가 90점 이상일 때: A 2) 점수가 90점 미만 80점 이상일 때: B 3) 점수가 80점 미만 70점 이상일 때: C 4) 점수가 70점 미만: F

import sys
input = lambda: int(sys.stdin.readline().strip())

score = input()
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else:
    print('F')