from collections import deque

def solution(queue1, queue2):
    deque1 = deque(queue1)
    deque2 = deque(queue2)
    Q1sum = sum(queue1)
    Q2sum = sum(queue2)

    queueSize = len(deque1)
    answer = 0
    for i in range(queueSize * 2 + 10) :
        if len(deque2) == 0 or len(deque1) == 0 :
            return -1
        if Q1sum > Q2sum :
            popleft = deque1.popleft()
            Q1sum -= popleft
            deque2.append(popleft)
            Q2sum += popleft
            answer += 1
        elif Q1sum < Q2sum :
            popleft = deque2.popleft()
            Q2sum -= popleft
            deque1.append(popleft)
            Q1sum += popleft
            answer += 1
        else:
            return answer

    return -1






print( solution([1000000000, 1000000000], [1000000000, 1000000002]))