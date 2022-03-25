# 기쁨초등학교 수련회 현장입니다.
# 특별 레크리에이션 강사인 빈이는 장기자랑이 시작되기 전, 학생들의 흥을 높이기 위해 게임을 시작했습니다.
# 우선 학생들이 일렬로 줄을 섭니다.
# 예를 들어 강사가 숫자 3과 7을 외치면 줄을 3번째에 선 학생부터 7번째에 선 학생까지 중에 몸무게가 가장 적은 학생이 앞으로 나옵니다.
# 레크리에이션 강사가 숫자를 외칠 때 앞으로 나오는 학생의 몸무게를 출력하세요.
import sys

n = int(sys.stdin.readline())
stu_weight = list(map(int, sys.stdin.readline().split()))
start, end = map(int, sys.stdin.readline().split()) 

print(min(stu_weight[start-1:end]))