def bubblesort(list):
    n = len(list)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]


if __name__ == "__main__":
    l = [2, 32, 1, 4, 434, 56.8]
    print('Before bubblesort: ', l)
    bubblesort(l)
    print('After bubblesort: ', l)