def Floyd_Warshall(n, m, fares) :
    INF = int(1e11)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0

    # 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
    for fare in fares:
        # A에서 B로 가는 비용은 C라고 설정
        a, b, c = fare
        graph[b][a] = c
        graph[a][b] = c

    # 점화식에 따라 플로이드 워셜 알고리즘을 수행
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    return graph

def solution(n, s, a, b, fares):
    graph = Floyd_Warshall(n, len(fares), fares)

    answer = int(1e11)
    for i in range(n+1) :
        answer= min(answer, graph[s][i] + graph[i][a] + graph[i][b])
    return answer

print( solution(6, 4, 6, 2,
         [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))


