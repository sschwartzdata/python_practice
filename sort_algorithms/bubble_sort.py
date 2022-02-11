def swap_check(swap_arr):
    n = len(swap_arr) - 1
    for i in range(0, n - 1):
        if swap_arr[i] > swap_arr[i + 1]:
            return True
        else:
            pass


def bubble_sort(sorting_arr):
    arr = sorting_arr
    n = len(sorting_arr) - 1
    need_swap = True
    while need_swap == True:
        for i in range(0, n):
            if arr[i] > arr[i + 1]:
                x = arr[i]
                y = arr[i + 1]
                arr[i] = y
                arr[i + 1] = x
            else:
                pass
        print(arr)
        need_swap = swap_check(arr)
    return arr


def main():
    sorting_arr = [2, -2, 6, 6896, 44, 6, 55, 5, 9, 5, 9, 4565, 0, -1, -545, 0, 6]
    try:
        bubble_sort(sorting_arr)
    except Exception as e:
        print(e)
    return 0


if __name__ == '__main__':
    main()
