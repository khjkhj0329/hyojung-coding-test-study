import math
def solution(n):
    num = math.sqrt(n) # 제곱을 구해주는 함수
    if num % 1 == 0: # n이 정수일 경우
        answer = (num+1)**2 # 더하기 1를 하고 제곱을 해준다
    else: # n이 정수가 아닐 경우
        return -1 # -1를 리턴
    return answer

# 출력문
print(solution(121))
print(solution(3))