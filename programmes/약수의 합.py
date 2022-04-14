def solution(n):
    answer = 0
    for i in range(1, n+1): # 1부터 n까지 범위
        if n % i == 0:  # n에서 i를 나눈 나머지가 0일 떄
            answer += i # answer에 나온 i의 값을 더한 후 저장
    return answer

# 출력문
print(solution(12))
print(solution(5))