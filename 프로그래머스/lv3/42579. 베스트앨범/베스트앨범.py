from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_plays=defaultdict(int) #장르별 재생횟수
    genre=defaultdict(list) #장르별 [재생횟수, 고유번호]
    
    for idx in range(len(genres)) :
        genre[genres[idx]].append([plays[idx], idx])
        genre_plays[genres[idx]]+=plays[idx]
        
    genre_plays=sorted(genre_plays.items(), key=lambda x:-x[1]) #재생횟수 많은순
    
    for key, value in genre_plays :
        genre[key].sort(key=lambda x:-x[0]) #재생횟수 내림차순 정렬
        for play, idx in genre[key][:2] :
            answer.append(idx)
    return answer