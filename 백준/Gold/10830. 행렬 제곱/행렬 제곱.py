def matrixMul(num):
    global N, arr
    if num == 1:
        for i in range(N):
            for j in range(N):
                arr[i][j] %= 1000
        return arr
    elif num % 2 == 1:
        tmp = [[0] * N for _ in range(N)]
        C = matrixMul(num - 1)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    tmp[i][j] += C[i][k] * arr[k][j]
                tmp[i][j] %= 1000
        return tmp
    else:
        tmp = [[0] * N for _ in range(N)]
        C = matrixMul(num // 2)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    tmp[i][j] += C[i][k] * C[k][j]
                tmp[i][j] %= 1000
        return tmp


N, A = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
res = matrixMul(A)

# 출력
for i in range(N):
    for j in range(N):
        print(res[i][j], end=" ")
    print()