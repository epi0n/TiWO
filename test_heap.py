import pytest

from heap import Heap

test_swap_data = {
    0: {
        'i': 1,
        'j': 2,
        'input_heap': [5, 2, 12, 4],
        'output_heap': [5, 12, 2, 4]
    },
}


@pytest.mark.parametrize("_heap,i,j,expected", [
    (test_swap_data[0]['input_heap'], test_swap_data[0]['i'], test_swap_data[0]['j'], test_swap_data[0]['output_heap']),
])
def test_swap(_heap, i, j, expected):
    Heap.swap(_heap, i, j)
    assert _heap == expected
