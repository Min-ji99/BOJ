def solution(record):
    answer = []
    nickname={}
    for r in record :
        r=r.split(" ")
        if r[0]=="Enter" :
            nickname[r[1]]=r[2]
        elif r[0]=="Change" :
            nickname[r[1]]=r[2]
    #print(nickname)
    
    for r in record :
        r=r.split(" ")
        if r[0]=="Enter" :
            answer.append(nickname[r[1]]+"님이 들어왔습니다.")
        elif r[0]=="Leave" :
            answer.append(nickname[r[1]]+"님이 나갔습니다.")
    return answer