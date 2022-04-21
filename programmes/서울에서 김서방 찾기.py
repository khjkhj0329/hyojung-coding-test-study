def solution(seoul):
    # seoul에서 index를 이용하여 Kim을 찾는다. 그리고 문자형으로 변환 시켜준다.
    kim = str(seoul.index("Kim"))
    answer = "김서방은 " + kim +"에 있다"
    return answer

# 출력문
print(solution(["Jane", "Kim"]))