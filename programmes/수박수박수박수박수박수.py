def solution(n):
    answer = ''
    su = '수'
    bak = '박'
    for i in range(n):
        if i % 2 == 0:  # n이 짝수일 떄
            answer += su  # su('수')를 더하기
        else:  # n이 짝수가 아닐 때(홀수 일 때)
            answer += bak  # bak('박')를 더하기
    return answer

# 출력문
print(solution(3))
print(solution(10))