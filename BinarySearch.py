class BinarySearch:
    def binary_search(self, array, low, high, key):
        while low <= high:
            mid = (low + high) // 2
            if key < array[mid]:
                high = mid - 1
                self.binary_search(array, low, high, key)
            elif key > array[mid]:
                low = mid + 1
                self.binary_search(array, low, high, key)
            else:
                return "Found"
        return "Not Found"


if __name__ == "__main__":
    binary_search_obj = BinarySearch()
    list1 = input("Enter Sorted list of values by space separated: ").split()
    list1 = list(map(int, list1))
    key_item = int(input("Enter key to search: "))
    result = binary_search_obj.binary_search(list1, 0, len(list1)-1, key_item)
    print(result)
