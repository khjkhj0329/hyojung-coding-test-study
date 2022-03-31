def solution(phone_number):
    answer = "*" * (len(phone_number)-4) + phone_number[-4:]
    # phone_number의 길이에서 4개의 문자열을 뺴주고 남은 문자열에 *를 곱해준다.
    # 폰 넘버에서 -4:(뒤에 4개의 문자열)까지의 문자열를 붙여준다.
    return answer

print(solution('01033334444'))
print(solution('027778888'))