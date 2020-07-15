def bubble_sort(a):
    l = len(a)-1
    for i in range(l):
        swap = False
        for j in range(0,l-i):
            if a[j]>a[j+1]:
                swap = True
                a[j],a[j+1] = a[j+1],a[j]
        if swap == False:
            break
    return a

a = [5,4,3,2,1]
print(bubble_sort(a))