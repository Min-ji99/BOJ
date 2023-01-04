from collections import defaultdict
from itertools import combinations

def solution(infos, queries):
    answer=[]
    info_dict=defaultdict(list)#key: 언어,직군,경력,소울푸드 value : 점수
    for info in infos : 
        info=info.split(' ')
        info_value=int(info[-1])
        info_key=info[:-1]
        for i in range(5) : #info로 만들 수 있는 모든 조합
            for c in combinations(info_key, i) :
                query=''.join(c)
                info_dict[query].append(info_value)
    
    for key in info_dict.keys() :
        info_dict[key].sort()
    
    for query in queries : 
        query=query.split(' ')
        score=int(query[-1])
        query=query[:-1]
        
        for i in range(3) :
            query.remove('and')
        while '-' in query :
            query.remove('-')
        query=''.join(query)

        #개수 count
        if query in info_dict:
            values=info_dict[query]
            if len(values) > 0 :
                start, end=0, len(values)
                while start<end :
                    mid=(start+end)//2
                    if values[mid]>=score :
                        end=mid
                    else:
                        start=mid+1
                answer.append(len(values)-start)
        else:
            answer.append(0)        
    return answer