def solution(answers):

    stu1 = [1, 2, 3, 4, 5] * 2000
    stu2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    cut_stu1 = 0
    cut_stu2 = 0
    cut_stu3 = 0

    for i in range(0, len(answers)):
        if stu1[i] == answers[i]:
            cut_stu1 += 1
        if stu2[i] == answers[i]:
            cut_stu2 += 1
        if stu3[i] == answers[i]:
            cut_stu3 += 1

    rank = [0, cut_stu1, cut_stu2, cut_stu3]
    cut_max = max(rank) #제일 많이 맞춘 갯수를 찾기
    answer = []
    for i in range(len(rank)):
        if rank[i] == cut_max:
            answer.append(i)
    return answer