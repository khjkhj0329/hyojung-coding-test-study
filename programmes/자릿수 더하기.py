def solution(n):
    answer = 0
    N = str(n)  # n을 문자열로 변환
    for i in N:
        answer += int(i)    # int형으로 변환하고 더하기
    return answer

# 출력문
print(solution(123))
print(solution(879))