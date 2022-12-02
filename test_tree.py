'''
2. Взявши за основу код домашнього завдання лекції 14, розробіть
набір тестів з використання бібліотеки рутезі для методів додавання
нових елементів, пошуку мінімального і максимального значень та
видалення елементів бінарного дерева.
'''

from tree_test import * 

def test_insert():
    try:
        assert main_insert([12, 6, 18, 4, 21, 11, 23]) == [12, 6, 18, 4, 21, 11, 23]
        print("test_insert complited sucsesfully")
    except:
        print("test_insert complited with error")
test_insert()

def test_max():
    try:
        assert main_max([12, 6, 18, 4, 21, 11, 23]) == 23
        print("test_max complited sucsesfully")
    except:
        print("test_max complited with error")
test_max()

def test_min():
    try:
        assert main_min([12, 6, 18, 4, 21, 11, 23]) == 4
        print("test_min complited sucsesfully")
    except:
        print("test_min complited with error")
test_min()

def test_del():
    try:
        assert main_del([12, 6, 18, 4, 21, 11, 23], 6) == [12, 6, 18, 4, 21, 11, None]
        print("test_del complited sucsesfully")
    except:
        print("test_del complited with error")
test_del()




