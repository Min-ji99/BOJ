def solution(numbers) :
    numbers.sort(key=lambda x:str(x)*3, reverse=True)
    if(numbers[0]==0) : return "0"
    return ''.join(map(str, numbers))