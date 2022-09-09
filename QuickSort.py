"""
Quicksort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element from the array
and partitioning the other elements into two sub-arrays, according to whether they are less than or
greater than the pivot.
"""


class QuickSort:
    def quick_sort(self, arr_list):
        if len(arr_list) <= 1:
            return arr_list
        pivot = arr_list.pop()
        items_lower = []
        items_greater = []
        for item in arr_list:
            if item < pivot:
                items_lower.append(item)
            else:
                items_greater.append(item)
        return self.quick_sort(items_lower) + [pivot] + self.quick_sort(items_greater)


if __name__ == "__main__":
    quicksort = QuickSort()
    array = input("Enter space separated unordered numbers:").split()
    array = list(map(int, array))
    sorted_array = quicksort.quick_sort(array)
    print(sorted_array)
