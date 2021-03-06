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

    def _heap_down(self, current_index):
        """Move node down if worse than child node."""
        if current_index < self.get_heap_size():
            left_child, right_child = (current_index * 2) + 1, (current_index * 2) + 2
            if left_child < self.get_heap_size() or right_child < self.get_heap_size():
                if right_child < self.get_heap_size():
                    if any([self._heap[current_index] < self._heap[left_child], self._heap[current_index] < self._heap[right_child]]):
                        if self._heap[left_child] > self._heap[right_child]:
                            self._swap(current_index, left_child)
                            self._heap_down(left_child)
                        else:
                            self._swap(current_index, right_child)
                            self._heap_down(right_child)
                elif left_child < self.get_heap_size():
                    if self._heap[current_index] < self._heap[left_child]:
                        self._swap(current_index, left_child)
                        self._heap_down(left_child)

    def _add_node(self, node):
        """Add a new node."""
        self._heap.append(node)
        self._size += 1

    def _remove_node(self):
        """Remove the top node."""
        self._heap[0] = self._heap[self.get_heap_size() - 1]
        self._heap.pop()
        self._size -= 1

    def create_heap(self, input_heap):
        """Initializes the heap."""
        self._heap = input_heap
        self._size = len(input_heap)

    def set_heap_size(self, size):
        """Set heap size."""
        self._size = size

    def get_heap_size(self):
        """Returns heap size."""
        return self._size if self._size >= 0 else 0

    def insert(self, node):
        """Adds a new element to the heap."""
        self._add_node(node)
        self._heap_up(self.get_heap_size() - 1)
        self._heap_down(0)

    def pop(self):
        """Removes top element from the heap."""
        if self.get_heap_size() > 0:
            self._remove_node()
            self._heap_down(0)

    def print_heap(self):
        print(f'''\
        Heap size: {self.get_heap_size()}
        Heap structure: {self._heap}
        ''')


