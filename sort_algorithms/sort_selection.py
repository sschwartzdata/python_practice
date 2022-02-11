def min_index(arr, k):
    arr_len = len(arr)
    min_index = k
    for j in range(k + 1, arr_len):
        if arr[j] < arr[min_index]:
            # print(arr[min_index])
            # print(arr[j])
            min_index = j
    return min_index


def sel_sort(arr):
    sorted_arr = arr
    k = 0
    n = len(arr) - 1
    for k in range(0, n):
        # finding the minimum number
        minimum_index = min_index(sorted_arr, k)
        new_min = sorted_arr[minimum_index]
        print(new_min)
        swap = sorted_arr[k]
        sorted_arr[k] = new_min
        sorted_arr[minimum_index] = swap
        print(sorted_arr)
    return sorted_arr


def main():
    arr = [2, -2, 6, 6896, 44, 6, 55, 5, 9, 5, 9, 4565, 0, -1, -545, 0, 6]
    try:
        sel_sort(arr)
    except Exception as e:
        print(e)
    return 0


if __name__ == '__main__':
    main()
