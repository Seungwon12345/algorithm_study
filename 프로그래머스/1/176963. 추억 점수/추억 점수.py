def solution(name, yearning, photo):
    answer = []
    for i in photo:
        score = 0
        for j in i:
            k = 0
            for n in name:
                if j == n:
                    score += yearning[k]
                k += 1
        answer.append(score)
                
    return answer