import random
import time

import pytest

from heap import Heap


def simple_example():
    print(f'''\
    ===SIMPLE EXAMPLE - inserting===''')
    hp = Heap()
    hp.print_heap()
    for i in range(7):
        num = random.randrange(1, 11)
        print(f' Inserting a new random element, range[1, 10]... {num}')
        hp.insert(num)
        time.sleep(1)
        hp.print_heap()
        time.sleep(1)
    while True:
        print('Simple example finished. Try again (y), or return to menu (n)?')
        inp = input()
        if inp == 'y':
            simple_example()
            return
        elif inp == 'n':
            return
        else:
            print('Wrong input provided. Try again.')


def advanced_example():
    print(f'''\
    ===ADVANCED EXAMPLE - 50 pop/insert operations===''')
    hp = Heap()
    hp.print_heap()
    for i in range(50):
        num = random.randrange(1, 1001)
        pop_or_ins = random.randrange(0, 2)
        if pop_or_ins == 0:
            print(f' Inserting a new random element, range[1, 1000]... {num}')
            hp.insert(num)
            time.sleep(0.5)
            hp.print_heap()
            time.sleep(1)
        else:
            print(' Popping element from the top of the heap...')
            hp.pop()
            time.sleep(0.5)
            hp.print_heap()
            time.sleep(1)
    while True:
        print('Advanced example finished. Try again (y), or return to menu (n)?')
        inp = input()
        if inp == 'y':
            advanced_example()
            return
        elif inp == 'n':
            return
        else:
            print('Wrong input provided. Try again.')


def print_tests():
    pytest.main(["-s", "test_heap.py", "-vv"])


def main():
    while True:
        print('''\
        #######################################################################
        Hello. This is a basic MAXHeap data structure implementation in Python3.
        Menu:
        1. Show a basic example of a max heap data structure creation.
        2. Show a more advanced example of a max heap data structure creation.
        3. Run py-test.
        4. Exit.
        #######################################################################''')
        _input = input()
        if _input == '1':
            simple_example()
        elif _input == '2':
            advanced_example()
        elif _input == '3':
            print_tests()
        elif _input == '4':
            exit()
        else:
            print('''\
            ========================================
            Wrong command entered. Please try again.
            ========================================''')


if __name__ == '__main__':
    main()