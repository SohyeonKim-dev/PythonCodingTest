# N, M을 공백을 기준으로 구분하여 입력 받기
# n = 행의 개수
# m = 열의 개수
n, m = map(int, input().split())


graph = []
for i in range(n):
    # 행 단위로 입력
    graph.append(list(map(int, input())))


# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
# 깊이 우선 탐색 -> 가장 깊게 들어가는 ! 

def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    # 0부터 세기 때문에 n-1까지 count
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리 -> 1로 표시
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출 (왜?)
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        # 상하 좌우로 호출시킨 뒤, true 반환!
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        # 이게 어떻게 DFS가 되는지 이해 잘 안됨
        if dfs(i, j) == True:
            result += 1

print(result)
