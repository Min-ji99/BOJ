from collections import defaultdict

def solution(id_list, report, k):
    answer = [0]*len(id_list)
    
    report_dict=defaultdict(set)
    
    for r in report :
        r=r.split()
        report_dict[r[1]].add(r[0])
     
    for key, value in report_dict.items() :
        if len(value)>=k:
            for v in value:
                answer[id_list.index(v)]+=1
    return answer
