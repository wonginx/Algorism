def insertion_sort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
    

    
    return arr


def selection_sort(arr):
    for a in range(len(arr) -1):
        min = arr
        for b in range(a+1, len(arr)):
            if arr[b] < arr[min]:
                min = b
        arr[a], arr[min] = arr[min], arr[a]
    return [arr]

def bubble_sort():
    #버블정렬 함수

    return []

n = int(input())
num_list = []

for _ in range(n):
    num = int(input())
    num_list.append(num)

insertion_sorted_list = insertion_sort()
print(" ".join(map(str, insertion_sorted_list)))

selection_sorted_list = selection_sort()
print(" ".join(map(str, selection_sorted_list)))

bubble_sorted_list = bubble_sort()
print(" ".join(map(str, bubble_sorted_list)))