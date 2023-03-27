def pop(tmp, board) :#블록 제거
    for i, j in tmp :
        board[i][j]=" "

def down(m, n, board) : #내리기
    for i in range(n) :
        for j in range(m-1, 0, -1) :
            for k in range(j, -1, -1) :
                if board[j][i]==" " and board[k][i]!=" " :
                    board[j][i]=board[k][i]
                    board[k][i]=" "
                    break     
                    
def solution(m, n, board):
    answer = 0
    board=[list(map(str, b.rstrip())) for b in board]
    
    while True :
        flag=False #블록이 지워졌는지 check 변수
        tmp=set() #지워질 블록 좌표
        for i in range(m-1) :
            for j in range(n-1) :
                if board[i][j]==" " : continue
                
                if board[i+1][j]==board[i][j] and board[i][j+1]==board[i][j] and board[i+1][j+1]==board[i][j] :
                    tmp.add((i+1, j))
                    tmp.add((i, j))
                    tmp.add((i, j+1))
                    tmp.add((i+1, j+1))
                    
        
        if len(tmp)>0 :
            answer+=len(tmp) #지울 블록 개수
            pop(tmp, board)
        else:
            return answer
        down(m, n, board)
        '''
        for i in range(m) :
            print(*board[i])
        print("---------")
        '''
    return answer