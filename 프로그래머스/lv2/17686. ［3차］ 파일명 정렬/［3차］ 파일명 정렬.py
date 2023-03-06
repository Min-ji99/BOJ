def solution(files):
    answer = []
    
    file_seq=[]
    for idx, file in enumerate(files) :
        head, num, tail = '','',''
        file=file.lower()
        for i in range(len(file)) :
            if file[i].isdigit():
                head = file[:i]
                num=file[i:]
                break
        for j in range(len(num)) :
            if not num[j].isdigit() :
                tail=num[j:]
                num=num[:j]
                break
        file_seq.append([head, num, tail, idx])

    file_seq.sort(key=lambda x:(x[0], int(x[1])))
    for file in file_seq :
        answer.append(files[file[3]])
    return answer