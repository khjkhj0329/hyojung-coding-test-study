def solution(n):
    answer = 0
    for i in range(1,n): # 범위(1부터 n전까지)
        if n % i == 1: # n에서 i를 나눈 나머지가 1일 때
            answer = i # i를 answer에 저장
            return answer

# 출력문
print(solution(10))
print(solution(12))