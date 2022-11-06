
def solution(survey, choices):

    dict = {
        "R" : 0,
        "T" : 0,
        "F" : 0,
        "C" : 0,
        "M" : 0,
        "J" : 0,
        "A" : 0,
        "N" : 0
    }
    for i in range(len(choices)) :
        if choices[i] > 4 :
            dict[survey[i][1]] += choices[i] - 4
        elif choices[i] < 4 :
            dict[survey[i][0]] += (choices[i] * -1) + 4

    answer = []
    answer.append("R") if dict["R"] >= dict["T"] else answer.append("T")
    answer.append("C") if dict["C"] >= dict["F"] else answer.append("F")
    answer.append("J") if dict["J"] >= dict["M"] else answer.append("M")
    answer.append("A") if dict["A"] >= dict["N"] else answer.append("N")


    answer = ''.join(answer)
    return answer

print( solution(	['AN', 'CF', 'MJ', 'RT', 'NA'], [5, 3, 2, 7, 5]))