class Heap:
    """Heap data structure. Implemented as a max heap - max element at the top. """
    def __init__(self):
        self._heap = []
        self._size = 0

    def __eq__(self, other):
        return self._heap == other._heap

    def _swap(self, i, j):
        """Swap child element with parent element."""
        tmp = self._heap[i]
        self._heap[i] = self._heap[j]
        self._heap[j] = tmp

    def _heap_up(self, i):
        """Move node up if better than parent node."""
        if i > 0:
            parent_index = int((i - 1) / 2)
            if self._heap[i] > self._heap[parent_index]:
                self._swap(i, parent_index)
            self._heap_up(parent_index)

    def _heap_down(self, i):
        """Move node down if worse than child node."""
        raise NotImplementedError

    def create_heap(self, input_heap):
        self._heap = input_heap
        self._size = len(input_heap)

    def set_heap_size(self, size):
        """Set heap size."""
        self._size = size

    def get_heap_size(self):
        """Returns heap size."""
        return self._size if self._size >= 0 else 0

    def insert(self):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError
