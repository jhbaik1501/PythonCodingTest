


from itertools import combinations

def 조합(items, course) :
    ret = []
    for i in course :
        cases = combinations(items, i)
        for case in cases :
            caseArr = list(case)
            caseArr.sort()
            ret.append(''.join(caseArr))
    return ret


def solution(orders, course):
    dict = {}

    for order in orders :
        for element in 조합(order, course) :
            if dict.get(element) is None :
                dict[element] = 1
            else :
                dict[element] += 1
    answer = []
    hashmap = {}

    for i in course :
        hashmap[i] = {
            "size" : 0,
            "items" : []
        }

    for item in dict :
        if hashmap[len(item)]["size"] < dict[item] :
            hashmap[len(item)]["size"] = dict[item]
            hashmap[len(item)]["items"] = [item]
        elif hashmap[len(item)]["size"] == dict[item] :
            hashmap[len(item)]["items"].append(item)

    for h in hashmap :
        if hashmap[h]["size"] >= 2 :
            for it in hashmap[h]["items"] :
                answer.append(it)
    answer.sort()
    return answer

print( solution(["XYZ", "XWY", "WXA"], [2, 3, 4]) )
# print( solution(	["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]) )