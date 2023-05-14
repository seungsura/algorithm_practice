def solution(absolutes, signs):
    
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:
            cnt = absolutes[i]
        else:
            cnt = -1 * absolutes[i]
        answer += cnt
    
    return answer