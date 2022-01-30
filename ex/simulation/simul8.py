def permutation(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in permutation(array[:i]+array[i+1:], r-1):
                yield [array[i]] + next
        
def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    
    answer = 9 # 문제에서 최대가 8
    for i in range(length):
        for d in permutation(dist, len(dist)):
            cnt = 1
            cover = weak[i] + d[cnt-1]
            for j in range(i+1, i+length):
                if cover < weak[j]:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    cover = weak[j] + d[cnt-1]
            answer = min(answer, cnt)
    
    if answer > len(dist):
        return -1
    return answer
    
n = int(input())
weak = list(map(int, input().split()))
dist = list(map(int, input().split()))
print(solution(n, weak, dist))