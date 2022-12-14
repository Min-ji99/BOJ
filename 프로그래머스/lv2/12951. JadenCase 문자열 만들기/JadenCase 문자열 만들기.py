def solution(s):
    answer = ''
    s1=s.lower()
    s2=s.upper()
    for i in range(len(s1)) :
        if i==0 or s1[i-1]==" ":
            answer+=s2[i]
        else :
            answer+=s1[i]
    return answer
