def solution(arr, k):
    cal = lambda x: x * k if k % 2 != 0 else x + k
    return list(map(cal, arr))
