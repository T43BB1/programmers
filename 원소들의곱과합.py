def solution(num_list):
    mul = 1
    total = 0 
    for i in num_list:
        mul *= i
        total += i
    return int(mul < total ** 2)
    