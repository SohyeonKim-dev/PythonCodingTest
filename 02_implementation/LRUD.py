n = map(int, input().split())

moving = list(input().split())

x, y = 1, 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
move_types = ['L', 'R', 'U', 'D']

for plan in moving:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
      # 아.. 이게 이것만으로 해결이 가능하구나.. (틀 밖으로 나가는 경우만 고려하기)
        continue

    x, y = nx, ny

print(x, y)
