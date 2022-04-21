def solution(left, right):
    answer = 0
    for i in range(left, right+1):  # left ~ right까지의 범위
        count = 0
        for j in range(1, i+1):     # 1~(left~right)까지의 범위
            if i % j == 0:  # i와 j를 나눈 나머지가 0이면(약수)
                count += 1  # 1를 더해준다
        if count % 2 == 0:  # 약수의 갯수(count)가 짝수이면
            answer += i     # i를 answer에 더한 후 저장
        else:   # 짝수가 아니라면(홀수)
            answer -= i     #i를 answer에서 뺸 후 저장
    return answer

#출력문
print(solution(13, 17))
print(solution(24, 27))
