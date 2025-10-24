def insertion_sort_desc(arr):
    """
    Sorts a list of numbers in descending order using the Insertion Sort algorithm.
    
    Parameters:
        arr (list): A list of numerical values.

    Returns:
        list: The sorted list in descending order.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements smaller than the key to one position ahead
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    print("=== Insertion Sort (Descending Order) ===")
    
    # Allow user to enter a list of numbers
    try:
        user_input = input("Enter numbers separated by spaces (e.g., 12 11 13 5 6): ")
        numbers = [int(x) for x in user_input.split()]
    except ValueError:
        print("Invalid input! Please enter only integers.")
        exit(1)
    
    print(f"\nOriginal List: {numbers}")
    sorted_numbers = insertion_sort_desc(numbers)
    print(f"Sorted List (Descending): {sorted_numbers}")
