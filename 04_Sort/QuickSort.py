# 정석

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: 
        return
        # 종료 조건 

    pivot = start
    left = start + 1
    right = end
    
    while(left <= right):
        # while 문의 종료 조건
        # 피벗보다 큰 데이터를 찾을 때까지 반복 (왼쪽부터)
        while(left <= end & array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복 (오른쪽부터)
        while(right > start and array[right] >= array[pivot]):
            right -= 1

        if(left > right): # 엇갈림 처리
            array[right], array[pivot] = array[pivot], array[right]

        else: # 교체
            array[left], array[right] = array[right], array[left]

    # 재귀 진행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)




# 파이썬의 장점 (quick sort 2)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array
        # 리스트가 하나 이하의 원소만을 담고 있다면 종료

    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 각각 정렬을 수행하고, 전체 리스트를 생성 및 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
