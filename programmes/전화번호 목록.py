def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):  # 첫번쨰 번호부터
        j = len(phone_book[i])  # i를 j에 저장(같은지 찾을 떄 사용)
        if phone_book[i] == phone_book[i+1][:j]:    # i에 들었있는 전화번호의 [:j]가 같으면
            answer = False  # false를 answer에 저장
    return answer

# 출력문
print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))
