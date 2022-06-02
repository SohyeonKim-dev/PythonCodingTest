# 큰 수의 법칙

'''

배열의 크기 n
숫자가 더해지는 횟수 m 
연속 가능 횟수 k

'''

n = 5
m = 8
k = 3

list = [2, 4, 5, 4, 6]
empty_list = []

first_max = max(list)
list.pop(list.index(max(list)))
second_max = max(list)
count = 0

while (count < m):
  for _ in range(k):
    empty_list.append(first_max)
    count += 1
  empty_list.append(second_max)
  count += 1

print(empty_list)
