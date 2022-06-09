array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 임시 사용 및 0 - 9 순차적으로 refresh
# 정렬되는 순서가 index 따라서 순차적으로 진행되니까!
# 코딩 테스트에서 자주 쓰이는 방식!
# 선택 정렬이 효율은 떨어지지만, 해당 방식을 직접 작성할 줄 알아야 한다! :) 

for i in range(len(array)):
    min_index = i 
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # swap

print(array)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
