"""
Insertion sort is the simple method of sorting an array. In this technique,
the array is virtually split into the sorted and unsorted part.
An element from unsorted part is picked and is placed at correct position in the sorted part.
"""


class InsertionSort:
    @staticmethod
    def insertion_sort(unsorted_array):
        for i in range(1, len(unsorted_array)):
            k = unsorted_array[i]
            j = i - 1
            while j >= 0 and k < unsorted_array[j]:
                unsorted_array[j + 1] = unsorted_array[j]
                j -= 1
            unsorted_array[j + 1] = k

        return unsorted_array


if __name__ == "__main__":
    insertion_sort_obj = InsertionSort()
    list1 = input("Enter space separated unsorted values:").split()
    list1 = list(map(int, list1))
    result = insertion_sort_obj.insertion_sort(list1)
    print(result)
