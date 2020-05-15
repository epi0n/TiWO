import pytest

from heap import Heap

tmp_heap_1 = Heap()
tmp_heap_1._heap = [5, 2, 12, 4]
tmp_heap_2 = Heap()
tmp_heap_2._heap = [5, 12, 2, 4]
test_swap_data = {
    0: {
        'i': 1,
        'j': 2,
        'input_heap': tmp_heap_1,
        'expected_heap': tmp_heap_2
    },
}
tmp_expected_heap = Heap()
tmp_expected_heap._size = 5
test_set_heap_size_data = {
    0: {
        'input_heap': Heap(),
        'size': 5,
        'expected_heap': tmp_expected_heap
    }
}


@pytest.mark.parametrize("input_heap,i,j,expected_heap", [
    (test_swap_data[0]['input_heap'], test_swap_data[0]['i'], test_swap_data[0]['j'], test_swap_data[0]['expected_heap']),
])
def test_swap(input_heap, i, j, expected_heap):
    input_heap.swap(i, j)
    assert input_heap == expected_heap


@pytest.mark.parametrize("input_heap,size,expected_heap", [
    (test_set_heap_size_data[0]['input_heap'], test_set_heap_size_data[0]['size'], test_set_heap_size_data[0]['expected_heap']),
])
def test_set_heap_size(input_heap, size, expected_heap):
    input_heap.set_heap_size(size)
    assert input_heap._size == expected_heap._size

