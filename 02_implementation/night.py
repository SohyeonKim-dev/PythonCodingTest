# 현재 위치
input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1
# ord 내장함수? 

# 8가지 이동 방향
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]


result = 0
for step in steps:
  # 쭉 훑으면 가능하니깐! (모든 step 체크)
  next_row = row + step[0]
  next_col = col + step[1]
  if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
    # 조건 확인 
    result += 1

print(result)


'''

* python ord func
하나의 문자를 인자로 받음 -> 해당 문자에 해당하는 유니코드 정수를 반환
ex) ord('a')를 넣으면 정수 97을 반환

'''
