def solution(arr):
    if len(arr) > 1:    # arr의 길이가 1보다 크다면
        arr.remove(min(arr))    # min을 이용하여 제일 작은 수 제거
    else:   # arr의 길이가 1이하 이면
        arr = [-1]  #-1를 arr에 저장
    return arr

# 출력문
print(solution([4,3,2,1]))
print(solution([10]))