def solution(new_id):
    answer=''
    
    #1단계(대문자->소문자)
    new_id=new_id.lower()
    
    #2단계 문자 제거
    for c in new_id:
        if c.isalpha() or c.isdigit() or c=='-' or c=='_' or c=='.':
            answer+=c
    
    #3단계 마침표 2번 이상 치환
    while '..' in answer:
        answer=answer.replace('..', '.')
       
    #4단계 처음과 끝 마침표 제거
    if answer[0]==".":
        if len(answer)>=2 :
            answer=answer[1:]
        else:
            answer=''
            
    if len(answer)>=1 and answer[-1]==".":
        answer=answer[:-1] 
        
    #5단계
    if len(answer)==0 :
        answer+='a'
        
    #6단계
    if len(answer)>=16:
        answer=answer[:15]
    if answer[-1]=='.':
        answer=answer[:-1]
    
    #7단계
    while len(answer)<=2 :
        answer+=answer[-1]
    
    print(answer)
    
    return answer