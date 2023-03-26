from sort_scripts import SortAlgos

import time

class Recursion(SortAlgos):

    def __init__(self, arr):
        SortAlgos.__init__(self, arr)
        # Super().__init__(self, arr)
        
    
    def factorial(self, n):
        start = time.process_time()
        """0, 1, 2, 3, 6, 18, 13"""
        if n < 2:
            start = time.process_time()
            return 1
        
        return n * self.factorial(n - 1)

    def fibonacci(self, n):
        """0, 1, 2, 3, 5, 8"""
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return self.fibonacci(n-1) + self.fibonacci(n-2)
    
    
        