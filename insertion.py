

def insertion_sort(x):
    for j in range(1, len(x)-1):
        key = x[j]
        i = j - 1
        while i > -1 and x[i] > key:
            x[i+1] = x[i]
            i -= 1
        x[i+1] = key
    return x



