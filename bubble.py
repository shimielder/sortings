def bubble_sort(x):

    for i in range(len(x)-1):
        for k in range(len(x)-i-1):
            if x[k] > x[k + 1]:
                x[k], x[k + 1] = x[k + 1], x[k]
                k = 0
    return x