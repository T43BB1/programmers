def solution(my_string, alp):
    new_str = ""
    for i in range(0,len(my_string)):
        if my_string[i].upper() == alp.upper() : new_str += my_string[i].upper()
        else: new_str += my_string[i]
    return new_str
