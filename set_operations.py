"""
Set Operations Module
Handles set theory operations: Union, Intersection, Difference, and Cardinality.
"""


class SetOperations:
    """Performs various set operations."""
    
    @staticmethod
    def union(set_a, set_b):
        """
        Returns the union of two sets (A ∪ B).
        Contains all elements from both sets.
        """
        return set_a | set_b
    
    @staticmethod
    def intersection(set_a, set_b):
        """
        Returns the intersection of two sets (A ∩ B).
        Contains only elements present in both sets.
        """
        return set_a & set_b
    
    @staticmethod
    def difference(set_a, set_b):
        """
        Returns the difference of two sets (A - B).
        Contains elements in A but not in B.
        """
        return set_a - set_b
    
    @staticmethod
    def cardinality(set_a):
        """
        Returns the cardinality of a set (|A|).
        The number of elements in the set.
        """
        return len(set_a)

