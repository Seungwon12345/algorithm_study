def solution(number):
    answer = 0
    list(number)
    for i in range(len(number)):
        for j in range(i+1, len(number)):
            for n in range(j+1, len(number)):
                if number[i] + number[j] + number[n] == 0:
                    answer += 1
        
    
    return answer