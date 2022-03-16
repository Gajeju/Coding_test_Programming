# 정수 형태의 원의 반지름 R이 입력되었을 때 원의 넓이를 출력하는 프로그램을 작성하세요.
# 원주율(PI)의 값은 3.14라고 가정하며 결과가 실수인 경우 최대 소수점 이하 둘째 자리까지 출력합니다.

import sys

r = float(sys.stdin.readline())
PI = 3.14
area = r * r * 3.14
# print(area)
# print(round(area, 1))
# print(f'{area:.2f}')

if area == int(area):
    print(int(area))
elif area == round(area, 1):
    print(f'{area:.1f}')
else:
    print(f'{area:.2f}')