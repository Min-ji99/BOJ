from collections import defaultdict
def solution(clothes):
    cloth_type={}
    for name, types in clothes :
        cloth_type[types]=cloth_type.get(types, 0)+1
    
    count=1
    for i in cloth_type.values() :
        count*=(i+1)
    
    return count-1