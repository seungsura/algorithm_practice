from collections import defaultdict

weights = [100,180,360,100,270]

def solution(weights):
    answer = 0
    dict1 = defaultdict(int)

    # dict에 추가
    for i in weights:
        dict1[i] += 1

    weights = set(weights)

    # 같은 수 세기
    for i in weights:
        if dict1[i] >= 2:
            answer += dict1[i] * (dict1[i] -1) // 2

    # 비율이 2:3, 2:4, 3:4인 수 세기
    for i in weights:
        if dict1[i * 2/3]:
            answer += dict1[i * 2/3] * dict1[i]
        if dict1[i * 2/4]:
            answer += dict1[i * 2/4] * dict1[i]
        if dict1[i * 3/4]:
            answer += dict1[i * 3/4] * dict1[i]
    
    return answer

print(solution(weights))
