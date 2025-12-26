"""
Sorting Algorithms Module
Implements Bubble Sort, Selection Sort, and Insertion Sort algorithms.
"""


class SortingAlgorithms:
    """Implements various sorting algorithms."""
    
    @staticmethod
    def bubble_sort(array):
        """
        Performs bubble sort on an array.
        
        Args:
            array: List to sort
        
        Returns:
            tuple: (sorted_array, steps)
        """
        arr = array.copy()
        n = len(arr)
        steps = []
        steps.append(f"Starting array: {arr}")
        
        for i in range(n):
            swapped = False
            steps.append(f"\nPass {i + 1}:")
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
                    steps.append(f"  Swapped {arr[j+1]} and {arr[j]}: {arr}")
            
            if not swapped:
                steps.append("  No swaps needed, array is sorted")
                break
        
        steps.append(f"\nFinal sorted array: {arr}")
        return arr, steps
    
    @staticmethod
    def selection_sort(array):
        """
        Performs selection sort on an array.
        
        Args:
            array: List to sort
        
        Returns:
            tuple: (sorted_array, steps)
        """
        arr = array.copy()
        n = len(arr)
        steps = []
        steps.append(f"Starting array: {arr}")
        
        for i in range(n):
            min_idx = i
            steps.append(f"\nPass {i + 1}: Finding minimum from index {i} to {n-1}")
            
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            
            if min_idx != i:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                steps.append(f"  Swapped {arr[i]} (min) with {arr[min_idx]}: {arr}")
            else:
                steps.append(f"  {arr[i]} is already in correct position")
        
        steps.append(f"\nFinal sorted array: {arr}")
        return arr, steps
    
    @staticmethod
    def insertion_sort(array):
        """
        Performs insertion sort on an array.
        
        Args:
            array: List to sort
        
        Returns:
            tuple: (sorted_array, steps)
        """
        arr = array.copy()
        n = len(arr)
        steps = []
        steps.append(f"Starting array: {arr}")
        
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            steps.append(f"\nPass {i}: Inserting {key} into sorted portion")
            
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
                steps.append(f"  Shifted {arr[j+1]} to the right: {arr}")
            
            arr[j + 1] = key
            if j + 1 != i:
                steps.append(f"  Inserted {key} at position {j + 1}: {arr}")
            else:
                steps.append(f"  {key} is already in correct position")
        
        steps.append(f"\nFinal sorted array: {arr}")
        return arr, steps

