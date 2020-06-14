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

    def _heap_up(self, current_index):
        """Move node up if better than parent node."""
        if current_index > 0:
            parent_index = int((current_index - 1) / 2)
            if self._heap[current_index] > self._heap[parent_index]:
                self._swap(current_index, parent_index)
            self._heap_up(parent_index)

    def _heap_down(self, i):
        """Move node down if worse than child node."""
        if i < self.get_heap_size():
            left_child, right_child = (i * 2) + 1, (i * 2) + 2
            if left_child < self.get_heap_size() or right_child < self.get_heap_size():
                if right_child < self.get_heap_size():
                    if any([self._heap[i] < self._heap[left_child], self._heap[i] < self._heap[right_child]]):
                        if self._heap[left_child] > self._heap[right_child]:
                            self._swap(i, left_child)
                            self._heap_down(left_child)
                        else:
                            self._swap(i, right_child)
                            self._heap_down(right_child)
                elif left_child < self.get_heap_size():
                    if self._heap[i] < self._heap[left_child]:
                        self._swap(i, left_child)
                        self._heap_down(left_child)

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
