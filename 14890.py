def checkArr(arr, L) :

    isRunway = [0 for i in range(len(arr) + 10)]

    target = arr[0]

    try :
        for i in range(len(arr)) :
            if target == arr[i]:
                continue
            elif target +1 == arr[i]:
                for j in range(i-1, i-L-1, -1) :

                    if j < 0 :
                        return False

                    if arr[j] is None or isRunway[j] == 1:
                        return False
                    isRunway[j] = 1
                    if arr[j] != target:
                        return False
                target = target + 1

            elif target -1 == arr[i]:
                for j in range(i, i+L) :
                    if arr[j] is None or isRunway[j] == 1:
                        return False

                    isRunway[j] = 1
                    if arr[j] != target - 1 :
                        return False
                target = target - 1
            else :
                return False
        return True
    except :
        return False


N, L = map(int, list(input().split()))

road = []
for i in range(N) :
    road.append(list(map(int, input().split())) )

ans = 0
for i in road :
    if checkArr(i, L) :
        ans += 1

for i in list(zip(*road)) :
    if checkArr(i, L):
        ans += 1

print(ans)



