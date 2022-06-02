n, m = map(int, input().split())

# n = 행의 개수 
# m = 열의 개수

empty_list = []

for i in range(n):
  data = list(map(int, input().split()))
  empty_list.append(min(data))

print(max(empty_list))
