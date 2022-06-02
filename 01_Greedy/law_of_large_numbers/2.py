# 입력 방식 익히기 
# 단순하게 푸는 답안 93 pg


n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

result = 0

while(1):
  for i in range(k):
    if m == 0:
      break
    result += first
    m -= 1

  if m == 0:
    break
  result += second
  m -= 1
  
print (result)
