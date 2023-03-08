def solution(s):
    answer = [0, 0]
    s=list(map(int, s.split(" ")))
    answer=[min(s), max(s)]
    return ' '.join(map(str, answer))