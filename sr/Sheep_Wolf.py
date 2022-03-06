max_sheep = 0
Info = []
tree = []

def dfs(Node, visited, sheep, wolf, nextNodeList):
    global max_sheep
    if visited[Node] == 1:
        return
    visited[Node] = 1
    
    if Info[Node] == 1:
        wolf += 1
    else:
        sheep += 1   
        
    max_sheep = max(max_sheep, sheep)
    
    if wolf >= sheep:
        return
    
    nextNodeList.extend(tree[Node])
    for nextNode in nextNodeList:
        dfs(nextNode, visited[:], sheep, wolf, [next_idx for next_idx in nextNodeList if next_idx != nextNode and visited[nextNode] == 0])
        

def solution(info, edges):
    global Info, max_sheep, tree
    visited = [0] * len(info)
    Info = info
    tree = [[] for _ in range(len(info))]
    for node1, node2 in edges:
        tree[node1].append(node2)
        
    dfs(0, visited, 0, 0, [])
    return max_sheep