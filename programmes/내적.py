def solution(a, b):
    answer = 0
    for i in range(len(a)): # a에 있는 수를 i에 집어넣기
        answer += a[i]*b[i] # a와 b를 하나씩 꺼내 곱해준 다음 answer 에 더해주기(반복)
    return answer

# 출력문
print(solution([1,2,3,4], [-3,-1,0,2]))
print(solution([-1,0,1], [1,0,-1]))