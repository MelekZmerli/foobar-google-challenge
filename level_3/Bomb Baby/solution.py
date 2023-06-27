def solution(x, y):
    M = max(int(x), int(y))
    F = min(int(x), int(y))
    generation = 0
    while M > 0 and F > 0:
        
        if M == 1 and F == 1: # Solution Found
            return str(generation)
            
        if F == 1: # for (X,1) cases need X-1 generations
            return str(generation + M - 1)
            
        generation += M//F 
        M, F = max(M%F,F), min(M%F,F)
        
    # No possible solution
    print("impossible")
