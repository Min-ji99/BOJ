def solution(book_time):

    # 풀이설명1 : 함수 만들기
    def change_min(str_time: str) -> int:
        return int(str_time[0:2]) * 60 + int(str_time[3:])
	
    #풀이 설명2 : 예약 시간이 빠른 순으로 정렬하기
    book_times = sorted([[change_min(i[0]), change_min(i[1]) + 10] for i in book_time])
	
    #풀이 설명3 : 방 배정하기
    rooms = []
    for book_time in book_times:
        if not rooms:
            rooms.append(book_time)
            continue
        for index, room in enumerate(rooms):
            if book_time[0] >= room[-1]:
                rooms[index] = room + book_time
                break
        else:
            rooms.append(book_time)
    return len(rooms)