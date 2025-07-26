def solution(n):
    answer = ''
    result = 0
    while n > 0:
        answer = str(n % 3) + answer
        n //= 3           
        

    for i in range(len(answer)):
        result += int(answer[i]) * (3**i)
    return result