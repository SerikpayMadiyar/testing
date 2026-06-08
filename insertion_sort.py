def bidirectional_selection_sort(arr):
    n = len(arr)
    # Left moves forward, right moves backward
    left = 0
    right = n - 1

    while left < right:
        min_idx = left
        max_idx = left

        # Find both the minimum and maximum in the unsorted segment
        for i in range(left + 1, right + 1):
            if arr[i] < arr[min_idx]:
                min_idx = i
            elif arr[i] > arr[max_idx]:
                max_idx = i

        # Swap the found minimum with the left-most unsorted element
        arr[left], arr[min_idx] = arr[min_idx], arr[left]

        # Critical Edge Case: If the maximum element was at the 'left' index,
        # it was just swapped to 'min_idx'. We must update max_idx.
        if max_idx == left:
            max_idx = min_idx

        # Swap the found maximum with the right-most unsorted element
        arr[right], arr[max_idx] = arr[max_idx], arr[right]

        # Shrink the boundaries of the unsorted subarray
        left += 1
        right -= 1

    return arr

# Example Usage
if __name__ == "__main__":
    data = [38, 14, 55, 2, 79, 14, 43, 5]
    print("Original array:", data)
    
    sorted_data = bidirectional_selection_sort(data)
    print("Sorted array:  ", sorted_data)
