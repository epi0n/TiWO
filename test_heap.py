import pytest

from heap import Heap

"""
TEST DATA
"""
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
test_get_heap_size_data = {
    0: {
        'input_heap': tmp_expected_heap,
        'expected_heap_size': 5
    }
}
heap_test_heap_up = Heap()
heap_test_heap_up.create_heap([1, 2, 3, 4, 5])
expected_heap_test_heap_up = Heap()
expected_heap_test_heap_up.create_heap([5, 1, 3, 4, 2])

heap_test_heap_down = Heap()
heap_test_heap_down.create_heap([1, 2, 3, 4, 5])
expected_heap_test_heap_down = Heap()
expected_heap_test_heap_down.create_heap([3, 2, 1, 4, 5])

heap_test_insert = Heap()
heap_test_insert.create_heap([5, 4, 3, 2, 1])
expected_heap_test_insert = Heap()
expected_heap_test_insert.create_heap([6, 4, 5, 2, 1, 3])

heap_test_pop = Heap()
heap_test_pop.create_heap([6, 4, 5, 2, 1, 3])
expected_heap_test_pop = Heap()
expected_heap_test_pop.create_heap([5, 4, 3, 2, 1])
"""
/TEST DATA
"""


@pytest.mark.parametrize("input_heap,i,j,expected_heap", [
    (test_swap_data[0]['input_heap'], test_swap_data[0]['i'], test_swap_data[0]['j'], test_swap_data[0]['expected_heap']),
])
def test_swap(input_heap, i, j, expected_heap):
    input_heap._swap(i, j)
    assert input_heap == expected_heap


@pytest.mark.parametrize("input_heap,size,expected_heap", [
    (test_set_heap_size_data[0]['input_heap'], test_set_heap_size_data[0]['size'], test_set_heap_size_data[0]['expected_heap']),
])
def test_set_heap_size(input_heap, size, expected_heap):
    input_heap.set_heap_size(size)
    assert input_heap._size == expected_heap._size


@pytest.mark.parametrize("input_heap,expected_heap_size", [
    (test_get_heap_size_data[0]['input_heap'], test_get_heap_size_data[0]['expected_heap_size']),
])
def test_get_heap_size(input_heap, expected_heap_size):
    assert input_heap.get_heap_size() == expected_heap_size


@pytest.mark.parametrize("input_heap,expected_heap,example_index", [
    (heap_test_heap_up, expected_heap_test_heap_up,  expected_heap_test_heap_up.get_heap_size() - 1),
])
def test_heap_up(input_heap, expected_heap, example_index):
    input_heap._heap_up(example_index)
    assert input_heap == expected_heap


@pytest.mark.parametrize("input_heap,expected_heap,example_index", [
    (heap_test_heap_down, expected_heap_test_heap_down,  0),
])
def test_heap_down(input_heap, expected_heap, example_index):
    input_heap._heap_down(example_index)
    assert input_heap == expected_heap


@pytest.mark.parametrize("input_heap,expected_heap,example_index", [
    (heap_test_insert, expected_heap_test_insert,  0),
])
def test_insert(input_heap, expected_heap, example_index):
    input_heap.insert(6)
    assert input_heap == expected_heap


@pytest.mark.parametrize("input_heap,expected_heap,example_index", [
    (heap_test_pop, expected_heap_test_pop,  0),
])
def test_pop(input_heap, expected_heap, example_index):
    input_heap.pop()
    assert input_heap == expected_heap
