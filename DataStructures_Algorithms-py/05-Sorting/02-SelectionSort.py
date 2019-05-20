def selectionsort(list):
    n = len(list)
    for i in range(n - 1):
        # j: 0 ~ n-2
        minIndex = i
        for j in range(i+1, n):
            if list[minIndex] > list[j]:
                list[j], list[minIndex] = list[minIndex], list[j]

if __name__ == "__main__":
    l = [2, 32, 1, 4, 434, 56.8]
    print('Before bubblesort: ', l)
    selectionsort(l)
    print('After bubblesort: ', l)
