def insertion_sort(arr):
    n = len(arr)
    for j in range(0, n):
        for i in range(0, j):
            if arr[j] <= arr[i]:
                arr.insert(i, arr[j])
                arr.pop(j + 1)
            else:
                pass
    print(arr)
    return arr


def main():
    sorting_arr = [2, -2, 6, 6896, 44, 6, 55, 5, 9,
                   5, 9, 4565, 0, -1, -545, 0, 6]
    try:
        insertion_sort(sorting_arr)
    except Exception as e:
        print(e)
    return 0


if __name__ == '__main__':
    main()
