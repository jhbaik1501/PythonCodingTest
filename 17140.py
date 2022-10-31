
def printArr(arr) :
    for i in arr :
        for j in i :
            print(j, end=" ")
        print()



def changeCol(arr, colNum, rowNum):
    result = []
    MaxCol = 0
    for row in range(rowNum):
        dict = {}
        for col in range(colNum):
            if arr[row][col] is None or arr[row][col] == 0:
                continue
            if arr[row][col] not in dict:
                dict[arr[row][col]] = 1
                continue
            dict[arr[row][col]] += 1
        dict = sorted(dict.items(), key=lambda item: (item[1], item[0]))
        # print(dict)
        temp = []
        for tup in dict:
            temp.append(tup[0])
            temp.append(tup[1])

        MaxCol = max(len(temp), MaxCol)
        result.append(temp)

    for i in result:
        while len(i) < MaxCol:
            i.append(0)
    # print("col정렬")
    return result, MaxCol

def changeRow(arr, colNum, rowNum) :
    result = []
    MaxRow = 0
    for col in range(colNum):
        dict = {}
        for row in range(rowNum) :
            if arr[row][col] is None or arr[row][col] == 0:
                continue
            if arr[row][col] not in dict :
                dict[arr[row][col]] = 1
                continue
            dict[arr[row][col]] +=1
        dict = sorted(dict.items(), key=lambda item : (item[1], item[0]))
        temp = []
        for tup in dict :
            temp.append(tup[0])
            temp.append(tup[1])

        MaxRow = max(len(temp), MaxRow)
        result.append(temp)

    for i in result :
        while len(i) < MaxRow :
            i.append(0)
    rowNum = MaxRow
    arr = list(zip(*result))
    # print("row 정렬")
    return list(zip(*result)), MaxRow



arr = []

colNum = 3
rowNum = 3

r,c,k = map(int, input().split())

for i in range(3) :
     arr.append(list(map(int, input().split())))
exitCode = 0

for i in range(101) :
    try:
        if arr[r-1][c-1] == k :
            print(i)
            exitCode = 1
            break
    except :
        pass

    if exitCode == 1 :
        break


    if colNum <= rowNum :
        arr, colNum = changeCol(arr, colNum, rowNum)
    else :
        arr, rowNum = changeRow(arr, colNum, rowNum)

if exitCode == 0 :
    print(-1)


'''
1 2 2
1 2 1
2 1 3
3 3 3
'''