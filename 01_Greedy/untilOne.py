n, k = map(int, input().split())

# n = 어떠한 수
# k = 나눌 수

# 역으로 생각해보면? (이미 k로 나눌 횟수는 정해져 있음!)
# 아 재미있어. . .! 어 이 없어.. ㅋㅋ;;

count = 0

while ( n > k):
  if (n//k != 0):
    n -= 1
    count += 1
  n = n % k
  count += 1


print(count)
