def greet(name):
    return f"Hello, {name}!"

def quicksort(arr):
    """Sorts a list using the QuickSort algorithm."""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)


def sum_numbers(a, b):
    print(f"Sum: {a + b}")


def main():
    numbers = [10, 7, 8, 9, 1, 5]
    sorted_numbers = quicksort(numbers)
    print(greet("Hello R R ..done this change manually"))
    print(f"Sorted numbers: {sorted_numbers}")
    sum_numbers(10, 20)


if __name__ == "__main__":
    main()