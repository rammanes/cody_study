

def binary_search(items, search_element, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if items[mid] == search_element:
            return mid
        elif items[mid] < search_element:
            low = mid + 1
        else:
            high = mid - 1


array = [3, 4, 5, 6, 7]
element = 6
result = binary_search(array, element, 0, len(array)- 1)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")