def solution(x):
    sum = 0
    stx = str(x)
    for i in stx:
        sum += int(i)   # i의 숫자 자릿수를 더하기
        if x % sum == 0:    # x(10)에서 sum(자릿수 더한거)의 나머지가 0일 떄
            answer = True   # True를 answer에 저장
        else:               # x(10)에서 sum(자릿수 더한거)의 나머지가 0이 아닐 때
            answer = False  # False를 answer에 저장
    return answer

# 출력문
print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))