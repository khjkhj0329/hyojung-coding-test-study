from itertools import combinations
def solution(nums):
    answer = 0
    com = list(combinations(nums, 3)) # cimbinations 함수는 list를 조합
    for i in range(len(com)):
        total = sum(com[i])     # 조합한(com)를 더해준다.
        isPrime = True      # isPrime는 소수를 판별해준다. True = 소수 False = 소수X
        for j in range(2, total):      # 2,3,4...(total - 1)
            if total % j == 0:      # total를 i로 나누고 값이 0이면
                isPrime = False     # 소수가 아니다
                break # 빠져나오기
        if isPrime == True:     # 소수 이면
            answer += 1     # 1씩 카운트
    return answer

# 출력문
print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))