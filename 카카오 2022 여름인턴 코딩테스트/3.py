def solution(alp, cop, problems):
    answer = 0

    max_alg = -1
    max_cop = -1
    for i in range(len(problems)) :
        max_alg = max(problems[i][0], max_alg)
        max_cop = max(problems[i][1], max_cop)

    print(max_cop, max_alg)

    return answer



solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]])
solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]])
solution(0, 0, [[0, 1000, 1, 1, 1]])