# quich search algorithm
# takes a !sorted! array and an item and returns its position there

def bin_search(array, item):
    low = 0
    high = len(array) - 1
    while low <= high:
        middle = (low + high) // 2
        guess = array[middle]
        if guess == item:
            return middle
        elif guess < item:
            low = middle + 1
        else:
            high = middle - 1
    return None

