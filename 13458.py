import math

N = int(input())
AList = list(map(int, input().split()))
B, C = map(int, input().split())

ans = 0
for i in range(len(AList)) :
    AList[i] -= B
    ans += 1
for A in AList :
    if A > 0 :
        a_c = math.ceil(A / C)
        ans += a_c

print(ans)