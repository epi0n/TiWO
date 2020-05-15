class Heap:
    def __init__(self):
        self._heap = []

    @staticmethod
    def swap(_heap, i, j):
        """Swap child element with parent element."""
        tmp = _heap[i]
        _heap[i] = _heap[j]
        _heap[j] = tmp
