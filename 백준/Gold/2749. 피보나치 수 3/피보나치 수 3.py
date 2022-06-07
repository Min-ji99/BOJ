n=int(input())
mod=1000000
fibo=[0, 1]
n=n%(15*100000)
for i in range(n) :
    fibo[0], fibo[1]=fibo[1]%1000000, (fibo[0]+fibo[1])%1000000

print(fibo[0])