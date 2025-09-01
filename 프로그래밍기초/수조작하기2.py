 def solution(numLog):
    control = ''
    for i in range(1,len(numLog)):
        cal = numLog[i] - numLog[i-1] 
        if cal == 1: control += 'w'
        elif cal == -1: control += 's'
        elif cal == 10: control += 'd'
        elif cal == -10: control += 'a'
    
    return ''.join(control)
