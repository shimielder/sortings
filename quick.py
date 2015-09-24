"""Небольшой модуль с реализацией быстрой сортировки"""

def quick_sort(lst):
    less = []
    equal = []
    greater = []

    if len(lst) > 1:
        pivot = lst[0]
        for x in lst:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quick_sort(less)+equal+quick_sort(greater)
    else:
        return lst

def qsort(L):
    if L: return qsort([x for x in L if x<L[0]]) + [x for x in L if x==L[0]] + qsort([x for x in L if x>L[0]])
    return []