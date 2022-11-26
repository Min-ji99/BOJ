def solution(n, arr1, arr2):
    answer = [[] for _ in range(len(arr1))]
    maps=[]
    for i in range(len(arr1)):
        maps.append(bin(arr1[i] | arr2[i]))
    for i in range(len(maps)) :
        line=''
        for j in range(2, len(maps[i])) :
            if maps[i][j]=='1' :
                line+='#'
            else:
                line+=' '
        while len(line)<len(maps) :
            line=' '+line
        answer[i]=line
    return answer