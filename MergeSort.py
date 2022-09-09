"""
Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves,
calls itself for the two halves and then merges the two sorted halves.
The merge() function is used for merging two halves
"""


class MergeSort:
    def merge_sort(self, unsorted_list):
        if len(unsorted_list) > 1:
            mid = len(unsorted_list) // 2
            left = unsorted_list[:mid]
            right = unsorted_list[mid:]

            # Recursive call on each half
            self.merge_sort(left)
            self.merge_sort(right)

            # Two iterators for traversing the two halves
            i = 0
            j = 0

            # Iterator for the main list
            k = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    # The value from the left half has been used
                    unsorted_list[k] = left[i]
                    # Move the iterator forward
                    i += 1
                else:
                    unsorted_list[k] = right[j]
                    j += 1
                # Move to the next slot
                k += 1

            # For all the remaining values from left
            while i < len(left):
                unsorted_list[k] = left[i]
                i += 1
                k += 1

            # For all the remaining values from right
            while j < len(right):
                unsorted_list[k] = right[j]
                j += 1
                k += 1
        return unsorted_list


if __name__ == "__main__":
    merge_sort_obj = MergeSort()
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    merge_sort_obj.merge_sort(my_list)
    print(my_list)
