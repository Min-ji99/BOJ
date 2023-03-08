def solution(gems):
    answer = [0, len(gems)]
    gem_kind = len((set(gems)))  # 보석 종류 개수
    n = len(gems)
    start, end = 0, 0
    gem_dict = {gems[0]: 1}

    while start < n and end < n:
        if len(gem_dict) == gem_kind:
            if end - start < answer[1] - answer[0]:
                answer = [start+1, end+1]
            else:
                gem_dict[gems[start]] -= 1
                if gem_dict[gems[start]]==0:
                    del gem_dict[gems[start]]
                start += 1
        else:
            end += 1
            if end==n : break
            gem_dict[gems[end]] = gem_dict.get(gems[end], 0)+1
    return answer