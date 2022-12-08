from collections import defaultdict

def solution(genres, plays):
    answer=[]
    genres_count=defaultdict(int)
    genres_idx=defaultdict(list)
    for i in range(len(genres)) :
        genres_count[genres[i]]+=plays[i]
        genres_idx[genres[i]].append([plays[i], i])
    genres_count=sorted(genres_count, key=lambda x:-genres_count[x])
    for genre in genres_count :
        genre_list=genres_idx[genre]
        genre_list.sort(key=lambda x:(-x[0], x[1]))
        print(genre_list)
        count=0
        for play, idx in genre_list :
            count+=1
            if count>2 :
                break
            answer.append(idx)

    return answer
