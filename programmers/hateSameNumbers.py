def solution(arr):
    answer = []
    
    for num in arr:
        if not answer or answer[-1] != num:
            answer.append(num)

    return answer

arr = [1,1,3,3,0,1,1]
#arr = [4,4,4,3,3]
answer = solution(arr)
print(answer)