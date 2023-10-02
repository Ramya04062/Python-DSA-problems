def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
input_list = [5, 2, 9, 1, 5, 6]
sorted_list = insertion_sort(input_list.copy())
print("Sorted Array:", sorted_list)
