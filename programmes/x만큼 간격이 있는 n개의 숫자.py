def solution(x, n):
    answer = []
    for i in range(1, 1001): # 범위
        if len(answer) < n: # answer의 길이가 n보다 작을 때
            answer.append(x*i) # x의 배수를 answer에 더해준다
    return answer

# 출력문
print(solution(2, 5))
print(solution(-4, 2))