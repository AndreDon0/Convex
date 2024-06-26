import unittest
from math import inf
from adint import Adint


class TestAdint(unittest.TestCase):

    # Создание числа работает корректно
    def test_adint_create1(self):
        ai = Adint(12)
        self.assertEqual(ai.x, 12)
        self.assertFalse(ai.INF)

    def test_adint_create2(self):
        ai = Adint(inf)
        self.assertEqual(ai.x, 0)
        self.assertTrue(ai.INF)

    # Прибавление / вычитаниев  числа / бесконечности корректно
    def test_adint_add1(self):
        ai = Adint(1)
        ai += 3
        self.assertEqual(ai.x, 4)
        self.assertFalse(ai.INF)

    def test_adint_add2(self):
        ai = Adint(9)
        ai += inf
        self.assertEqual(ai.x, 9)
        self.assertTrue(ai.INF)

    def test_adint_sub1(self):
        ai = Adint(6)
        ai -= 4
        self.assertEqual(ai.x, 2)
        self.assertFalse(ai.INF)

    def test_adint_sub2(self):
        ai = Adint(inf)
        ai -= inf
        self.assertEqual(ai.x, 0)
        self.assertFalse(ai.INF)

    def test_adint_multi1(self):
        ai = Adint(7)
        ai += inf
        ai -= inf
        self.assertEqual(ai.x, 7)
        self.assertFalse(ai.INF)

    def test_adint_multi2(self):
        ai = Adint(5)
        ai += 8
        ai -= 4
        self.assertEqual(ai.x, 9)
        self.assertFalse(ai.INF)

    def test_adint_multi3(self):
        ai = Adint(inf)
        ai += inf
        ai += 9
        ai -= inf
        self.assertEqual(ai.x, 9)
        self.assertTrue(ai.INF)

    # Тест корректного вывода значения при вызове
    def test_adint_repr1(self):
        ai = Adint(6)
        self.assertEqual(ai.__repr__(), str(6))

    def test_adint_repr2(self):
        ai = Adint(inf)
        self.assertEqual(ai.__repr__(), str(inf))

    # Тест корректной работы функции get
    def test_adint_get1(self):
        ai = Adint(6)
        self.assertEqual(ai.get(), 6)

    def test_adint_get2(self):
        ai = Adint(inf)
        self.assertEqual(ai.get(), inf)
