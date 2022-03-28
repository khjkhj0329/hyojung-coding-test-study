def solution(num):
    answer = ''
    if num % 2 == 0:  # num을 2로 나눈 나머지가 0일 때 'Even'를 answer에 저장
        answer = 'Even'
    else: # num을 2로 나눈 나머지가 0이 아닐 때 'Odd'를 answer에 저장
        answer = 'Odd'
    return answer

# 출력문
num1 = solution(2)
print(num1)
num2 = solution(5)
print(num2)