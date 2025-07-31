def solution(name, yearning, photo):
    answer = []
    for i in photo :
        score = 0
        for j in i :
            k = 0
            for t in name :
                if j == t :
                    score += yearning[k]
                k += 1
            

        answer.append(score)       
                    

    return answer