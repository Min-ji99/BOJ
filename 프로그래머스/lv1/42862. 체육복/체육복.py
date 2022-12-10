def solution(n, lost, reserve):
    new_lost=set(lost)-set(reserve)
    new_reserve=set(reserve)-set(lost)

    for student in new_reserve :
        if student-1 in new_lost:
            new_lost.remove(student-1)
        elif student+1 in new_lost :
            new_lost.remove(student+1)
    return n-len(new_lost)
