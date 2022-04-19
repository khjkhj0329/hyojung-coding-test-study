def solution(numbers):
    answer = 0
    for i in range(10): # i의 범위 설정
        if i not in numbers:    # i가 numbers안에 들어있지 않다면
            answer += i # i를 answer에 더하기(반복)
    return answer

# 출력문
print(solution([1,2,3,4,6,7,8,0]))
print(solution([5,8,4,0,6,7,9]))
