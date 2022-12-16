def solution(phone_book):
    answer = True
    phone_book.sort()
    
    start=phone_book[0]
    for i in range(1, len(phone_book)) :
        if phone_book[i].startswith(start):
            return False
        else:
            start=phone_book[i]
    
    return answer