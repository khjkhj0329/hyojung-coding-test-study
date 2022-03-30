def solution(arr):
    answer = 0
    sum = 0 # 더한 수를 담는 곳
    for i in arr: # arr에 있는 수를 i에 담는다.
        sum += i # sum에 i(arr)를 하나씩 꺼내어 더해준다.
        answer = sum / len(arr) # 더한 수에서 arr의 길이를 나눈다.
    return answer

# 출력문
print(solution([1, 2, 3, 4]))
print(solution([5, 5]))