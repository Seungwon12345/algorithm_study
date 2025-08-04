def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        n = commands[i][0]   # 2차원 배열 
        j = commands[i][1]
        k = commands[i][2]
        
        s_arr = sorted(array[n-1:j])
        answer.append(s_arr[k-1])
    return answer