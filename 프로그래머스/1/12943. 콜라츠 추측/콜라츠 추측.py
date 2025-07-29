def solution(num):
    count = 0
    while num != 1:
        if num == 1:
            return 0
        
        elif count == 500:
            return -1
        
        elif num % 2 == 0:
            num //= 2
            count += 1
            
        else:
            num = num * 3 + 1
            count += 1
            
    return count