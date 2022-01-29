def check(built):
    for x, y, a in built:
        if a == 0: # 기둥
            if not(y == 0 or [x, y-1, 0] in built or [x-1, y, 1] in built or [x, y, 1] in built): # 바닥, 기둥, 보의 끝 부분 위 x
                return False
        else: # 보
            if not([x, y-1 , 0] in built or [x+1, y-1, 0] in built or ([x-1, y, 1] in built and [x+1, y, 1] in built)):
                return False
    return True

def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 0: # 삭제
            answer.remove([x,y,a])
            if not check(answer): # 삭제 안됨
                answer.append([x,y,a])     
        else: # 설치
            answer.append([x,y,a])
            if not check(answer): # 설치 안됨
                answer.pop()   
    answer.sort()
    return answer

print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))