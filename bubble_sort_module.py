def bubble_sort(nlist):
    n = len(nlist)
    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):
            if nlist[j] > nlist[j+1]:
                nlist[j], nlist[j+1] = nlist[j+1], nlist[j]
                swapped = True
        if not swapped:
            break
    return nlist