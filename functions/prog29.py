def binary_search_recursive(lst, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        return binary_search_recursive(lst, target, low, mid - 1)
    else:
        return binary_search_recursive(lst, target, mid + 1, high)

l = [10, 20, 30, 40, 50, 60, 70]
target = 40
index = binary_search_recursive(l, target, 0, len(l) - 1)
print("Element found at index:", index)
