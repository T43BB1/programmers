def solution(n):
    if n==1: return [n]
    x = lambda x: x/2 if x%2==0 else 3*x+1
    return [n] + solution(x(n))