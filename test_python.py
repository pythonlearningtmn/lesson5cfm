"""
В модуле написать тесты для встроенных функций filter, map, sorted,
а также для функций из библиотеки math: pi, sqrt, pow, hypot.
Чем больше тестов на каждую функцию - тем лучше
"""
from math import pi, sqrt, pow, hypot, sin, cos, tan

def _filter(_list, cnt):
    res = list(filter(lambda x: x % cnt == 0, _list))
    return res

def test_filter():
    my_list = range(10)
    assert _filter(my_list, 1) == list(range(0, 10, 1))
    assert _filter(my_list, 2) == list(range(0, 10, 2))
    assert _filter(my_list, 3) == list(range(0, 10, 3))
    assert _filter(my_list, 4) == list(range(0, 10, 4))

def _map(_list, cnt):
    res = list(map(lambda x: x ** cnt, _list))
    return res

def test_map():
    my_list = range(5)
    assert _map(my_list, 1) == [0, 1, 2, 3, 4]
    assert _map(my_list, 2) == [0, 1, 4, 9, 16]
    assert _map(my_list, 3) == [0, 1, 8, 27, 64]
    assert _map(my_list, 4) == [0, 1, 16, 81, 256]

def _sorted(_list, cnt, rev=False):
    res = list(sorted(_list, key=lambda x: x[cnt], reverse=rev))
    return res

def test_sorted():
    my_list = ['hskdt', 'aljyr', 'mvjtl', 'qkjfh', 'zmjgf']
    assert _sorted(my_list, 0) == ['aljyr', 'hskdt', 'mvjtl', 'qkjfh', 'zmjgf']
    assert _sorted(my_list, 1) == ['qkjfh', 'aljyr', 'zmjgf', 'hskdt', 'mvjtl']
    assert _sorted(my_list, 3) == ['hskdt', 'qkjfh', 'zmjgf', 'mvjtl', 'aljyr']
    assert _sorted(my_list, -1, True) == ['hskdt', 'aljyr', 'mvjtl', 'qkjfh', 'zmjgf']

def test_pi():
    assert sin(pi) <= 1e-15
    assert cos(pi) == -1
    assert tan(pi) <= 1e-15
    assert sin(pi / 2) == 1
    assert cos(pi / 2) <= 1e-15
    assert tan(pi * 2) <= 1e-15
    assert cos(pi * 2) <= 1

def test_sqrt():
    assert sqrt(4) == 2
    assert sqrt(9) == 3
    assert sqrt(16) == 4
    assert sqrt(100) == 10
    assert sqrt(256) == 16
    assert sqrt(1521) == 39
    assert sqrt(625681) == 791
    assert sqrt(6.25) == 2.5
    assert sqrt(189.8884) == 13.78

def test_pow():
    assert pow(2, 2) == 4
    assert pow(3, 3) == 27
    assert pow(10, 3) == 1000
    assert pow(5, -3) == 0.008
    assert pow(1.5, 3.5) == 4.133513940946613
    assert pow(3, 3.5) == 46.76537180435969
    assert pow(4, 1/2) == 2
    assert pow(27, 1/3) == 3
    assert pow(4, -1/2) == 0.5

def test_hypot():
    assert hypot(4, 1) == 4.123105625617661
    assert hypot(-2, 0) == 2.0
    assert hypot(-1, 2) == 2.23606797749979