def solution(xs):
    if len(xs) == 1: # if array contains one element, return its value
        return str(xs[0])
        
    active = [panel for panel in xs if panel != 0] # Remove panels with no power
    negative = [panel for panel in active if panel < 0] # Extract panels w/ negative power
    
    if len(negative)%2 != 0: # Applying 'trick' when odd number of panels with negative power
        negative.sort()
        active.remove(negative[-1]) # Remove panel with least negative power

    if not active: # if array contains only one negative panel and panels w/o power 
        return '0'
        
    power = 1
    for panel in active: # Multiplying power of final panels
        power *= panel
    return str(power)
