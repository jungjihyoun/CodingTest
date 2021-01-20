############ DFS 동작원리 : 스택 ###############
############     구현방법 : 재귀 함수 이용 ######



#DFS 메서드 정의
def dfs(graph, v , visited):
    visited[v] = True
    print(v , end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

#리스트 자료형으로 각 노드 연결 표시(2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

#각 노드가 방문된 정보 체크 (1차원 리스트)
visited = [False] * 9


dfs(graph,1,visited)