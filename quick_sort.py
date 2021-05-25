# quick sorting algorythm
# takes array and return it sorted in acsending order

def quick_sort(array):
    if len(array) < 2:
        return array
    pivot = array[len(array) // 2]
    array.pop(len(array) // 2)
    less = []
    more = []
    for i in array:
        if i <= pivot:
            less.append(i)
        else:
            more.append(i)
    array_sorted = quick_sort(less) + [pivot] + quick_sort(more)
    return array_sorted 

