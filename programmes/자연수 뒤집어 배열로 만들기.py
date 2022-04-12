def solution(n):
    answer = []
    num = str(n)
    for i in num:
        answer.append(int(i))   # answer에 i를 int형으로 변환후 더하기
    answer.reverse()    # append한 answer에 있는 수를 역순으로 뒤집기
    return answer

# 출력문
print(solution(12345))