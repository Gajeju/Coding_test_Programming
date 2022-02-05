equation = input().split('-')
add_list = []

for num in equation:
    add_list.append(sum(map(int, num.split('+'))))

answer = add_list[0]

for i in range(1,len(add_list)):
    answer -= add_list[i]


print(answer)

# 잃어버린 괄호
# 식을 입력받으면 괄호를 써서 최소값을 만들어 리턴한다
# + 먼저 하고 - 를 한다?
