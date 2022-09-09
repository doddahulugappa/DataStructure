"""
The selection sort algorithm sorts an array by repeatedly finding the minimum element
(considering ascending order) from unsorted part and putting it at the beginning.
"""

class SelectionSort:
    def selection_sort(self, array, size):
        for step in range(size):
            min_idx = step

            for i in range(step + 1, size):

                # to sort in descending order, change > to < in this line
                # select the minimum element in each loop
                if array[i] < array[min_idx]:
                    min_idx = i

            # put min at the correct position
            array[step], array[min_idx] = array[min_idx], array[step]
        return array


if __name__ == "__main__":
    data = [-2, 45, 0, 11, -9]
    size = len(data)
    selection_sort_obj = SelectionSort()
    data = selection_sort_obj.selection_sort(data, size)
    print('Sorted Array in Ascending Order:')
    print(data)