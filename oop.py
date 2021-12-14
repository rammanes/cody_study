class BinarySearch:
    def __init__(self, items):
        self.items = array
        self.low = 0
        self.high = len(items) - 1

    def binary_search(self, search_element):
        while self.low <= self.high:
            mid = self.low + (self.high - self.low) // 2
            if self.items[mid] == search_element:
                return mid
            elif self.items[mid] < search_element:
                self.low = mid + 1
            else:
                self.high = mid - 1





array = [2, 4, 7, 9, 10]
element = 9
bsearch = BinarySearch(array)
result = bsearch.binary_search(element)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
