class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    @staticmethod
    def swap(_heap, i, j):
        """Swap child element with parent element."""
        tmp = _heap[i]
        _heap[i] = _heap[j]
        _heap[j] = tmp

    def set_heap_size(self, size):
        """Set heap size."""
        self._size = size
