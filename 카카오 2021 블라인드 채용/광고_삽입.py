import datetime
from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline


def splitTime(logs):
    startTimes = []
    for log in logs :
        startTime, endTime = log.split("-")

        startTimes.append([datetime.datetime.strptime(startTime, '%H:%M:%S'), datetime.datetime.strptime(endTime, '%H:%M:%S')])
    return startTimes


def timeToDateTime(time):
    return datetime.datetime.strptime(time, '%H:%M:%S')


def solution(play_time, adv_time, logs):

    play_time = timeToDateTime(play_time)
    adv_time = timeToDateTime(adv_time)

    Times = splitTime(logs)
    Times.sort(key=lambda x : x[0])

    for time in Times :
        endTime = adv_time - time[0]
        bisect_left(Times[0], endTime)




    # for time in Times :
    #     time[0] +=
    answer = ''
    return answer



print( solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]) )
