def solution(brown, yellow):
    answer = []
    area = brown + yellow
    
    for h in range(1, int(area**0.5)+1):
        if area % h == 0:
            w = area // h
            
            if (w-2) * (h-2) == yellow:
                return [w, h]
            
    return [w, h]
    