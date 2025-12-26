"""
Searching Algorithms Module
Implements Linear Search and Binary Search algorithms.
"""


class SearchingAlgorithms:
    """Implements various searching algorithms."""
    
    @staticmethod
    def linear_search(array, target):
        """
        Performs linear search on an array.
        
        Args:
            array: List to search in
            target: Value to search for
        
        Returns:
            tuple: (index, steps) where index is -1 if not found
        """
        steps = []
        for i, element in enumerate(array):
            steps.append(f"Checking index {i}: {element} {'=' if element == target else '≠'} {target}")
            if element == target:
                steps.append(f"✓ Found at index {i}!")
                return i, steps
        steps.append("✗ Target not found in array")
        return -1, steps
    
    @staticmethod
    def binary_search(array, target):
        """
        Performs binary search on a sorted array.
        
        Args:
            array: Sorted list to search in
            target: Value to search for
        
        Returns:
            tuple: (index, steps) where index is -1 if not found
        """
        steps = []
        left = 0
        right = len(array) - 1
        step_num = 1
        
        while left <= right:
            mid = (left + right) // 2
            mid_value = array[mid]
            
            steps.append(f"Step {step_num}: Checking middle element at index {mid} = {mid_value}")
            
            if mid_value == target:
                steps.append(f"✓ Found at index {mid}!")
                return mid, steps
            elif mid_value < target:
                steps.append(f"  {mid_value} < {target}, searching right half [{mid+1}..{right}]")
                left = mid + 1
            else:
                steps.append(f"  {mid_value} > {target}, searching left half [{left}..{mid-1}]")
                right = mid - 1
            
            step_num += 1
        
        steps.append("✗ Target not found in array")
        return -1, steps

