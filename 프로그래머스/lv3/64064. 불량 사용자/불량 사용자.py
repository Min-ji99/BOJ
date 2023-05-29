from itertools import permutations

def check(users, banned_id) :
    for i in range(len(banned_id)) :
        if len(users[i])!=len(banned_id[i]):
            return False
        for idx in range(len(users[i])) :
            if banned_id[i][idx]!='*' and banned_id[i][idx]!=users[i][idx]:
                return False
    return True

def solution(user_id, banned_id):
    answer = []

    for users in list(permutations(user_id, len(banned_id))) :
        if check(users, banned_id) :
            if set(users) not in answer:
                answer.append(set(users))
    print(answer)
    return len(answer)
