class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def __eq__(self, other):
        return self._heap == other._heap

    def swap(self, i, j):
        """Swap child element with parent element."""
        tmp = self._heap[i]
        self._heap[i] = self._heap[j]
        self._heap[j] = tmp

    def set_heap_size(self, size):
        """Set heap size."""
        self._size = size

    def get_heap_size(self):
        """Returns heap size."""
        return self._size
