def Arrow(d):
    if d == 0 :
        return [0, 1]
    elif d == 1 :
        return [-1, 0]
    elif d == 2 :
        return [0, -1]
    else :
        return [1, 0]

def NextArrow(arrowList) :
    tempArr = []
    for arrow in arrowList :
        if arrow == [0, 1] :
            tempArr.append([-1, 0])
        elif arrow == [-1, 0]:
            tempArr.append([0, -1])
        elif arrow == [0, -1]:
            tempArr.append([1, 0])
        elif arrow == [1, 0]:
            tempArr.append([0, 1])
    tempArr.reverse()

    for temp in tempArr :
        arrowList.append(temp)
    return tempArr, arrowList


def printArr(arr) :
    for i in arr :
        for j in i :
            print(j, end=" ")
        print()


arr = [[0] * 102 for _ in range(102)]

N = int(input())

for _ in range(N) :
    y, x, d, g = list(map(int, input().split()))
    arrowList = []
    arrow = Arrow(d)
    arrowList.append(arrow)
    arr[x][y] = 1
    x += arrow[0]
    y += arrow[1]
    arr[x][y] = 1
    for i in range(g):
        moveArr, arrowList = NextArrow(arrowList)
        for move in moveArr :
            x += move[0]
            y += move[1]
            arr[x][y] = 1
        # printArr(arr)
        # print()

answer = 0
for i in range(len(arr) -1) :
    for j in range(len(arr) -1) :
        if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1] :
            answer += 1

print(answer)