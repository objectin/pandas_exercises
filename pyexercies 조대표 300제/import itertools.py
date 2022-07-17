import itertools

def solution(mylist):
    mylist.sort()

    answer = list(itertools.permutations(mylist, len(mylist)))
    
    return answer

print(solution)

