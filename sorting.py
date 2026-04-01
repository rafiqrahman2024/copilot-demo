def quicksort(arr):
    """Sorts a list using the QuickSort algorithm."""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)


# Example usage
if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90, 88, 45]
    sorted_numbers = quicksort(numbers)
    print(f"Original: {numbers}")
    print(f"Sorted:   {sorted_numbers}")