# 외로운 현우는 미소녀 연애 시뮬레이션 게임을 하려고 합니다.
# 다운로드를 끝내고 게임에 접속하니 아이디를 만들라는 창이 등장했습니다.
# 아이디는 영어로만 쓸 수 있고, 20글자를 넘어가면 안 됩니다. 현우가 정한 아이디의 생성 가능여부를 출력하세요.
import sys

id = sys.stdin.readline()

if len(id) > 20:
    print('I')
else:
    print('P')