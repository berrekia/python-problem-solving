
class SortAlgos:
    def __init__(self, arr):
        self.arr = arr

    def check_type(self):
        return all(isinstance(x, str) for x in self.arr)

    def sort_strings(self):
        return self.arr.sort(key=len)

    def bubble_sort(self):
        """Tri de bulles"""
        for i in self.arr:
            pass


