import unittest
from unittest.mock import patch
from math import sqrt, inf
from r2point import R2Point


class TestR2Point(unittest.TestCase):

    # Точку можно создать через стандартный поток ввода
    def test_r2point_input(self):
        coords = iter(["1", "2"])
        with patch('builtins.input', lambda _: next(coords)):
            self.assertEqual(R2Point(), R2Point(1.0, 2.0))

    # Расстояние от точки до самой себя равно нулю
    def test_dist1(self):
        a = R2Point(1.0, 1.0)
        self.assertAlmostEqual(a.dist(R2Point(1.0, 1.0)), 0.0)

    # Расстояние между двумя различными точками положительно
    def test_dist2(self):
        a = R2Point(1.0, 1.0)
        self.assertAlmostEqual(a.dist(R2Point(1.0, 0.0)), 1.0)

    def test_dist3(self):
        a = R2Point(1.0, 1.0)
        self.assertAlmostEqual(a.dist(R2Point(0.0, 0.0)), sqrt(2.0))

    # Площадь треугольника равна нулю, если все вершины совпадают
    def test_area1(self):
        a = R2Point(1.0, 1.0)
        self.assertAlmostEqual(R2Point.area(a, a, a), 0.0)

    # Площадь треугольника равна нулю, если все вершины лежат на одной прямой
    def test_area2(self):
        a, b, c = R2Point(0.0, 0.0), R2Point(1.0, 1.0), R2Point(2.0, 2.0)
        self.assertAlmostEqual(R2Point.area(a, b, c), 0.0)

    # Площадь треугольника положительна при обходе вершин против часовой
    # стрелки
    def test_area3(self):
        a, b, c = R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(1.0, 1.0)
        self.assertGreater(R2Point.area(a, b, c), 0.0)

    # Площадь треугольника отрицательна при обходе вершин по часовой стрелке
    def test_area4(self):
        a, b, c = R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(1.0, 1.0)
        self.assertLess(R2Point.area(a, c, b), 0.0)

    # Точки могут лежать внутри и вне "стандартного" прямоугольника с
    # противоположными вершинами (0,0) и (2,1)
    def test_is_inside1(self):
        a, b = R2Point(0.0, 0.0), R2Point(2.0, 1.0)
        self.assertTrue(R2Point(1.0, 0.5).is_inside(a, b))

    def test_is_inside2(self):
        a, b = R2Point(0.0, 0.0), R2Point(2.0, 1.0)
        self.assertTrue(R2Point(1.0, 0.5).is_inside(b, a))

    def test_is_inside3(self):
        a, b = R2Point(0.0, 0.0), R2Point(2.0, 1.0)
        self.assertFalse(R2Point(1.0, 1.5).is_inside(a, b))

    # Ребро [(0,0), (1,0)] может быть освещено или нет из определённой точки
    def test_is_light1(self):
        a, b = R2Point(0.0, 0.0), R2Point(1.0, 0.0)
        self.assertFalse(R2Point(0.5, 0.0).is_light(a, b))

    def test_is_light2(self):
        a, b = R2Point(0.0, 0.0), R2Point(1.0, 0.0)
        self.assertTrue(R2Point(2.0, 0.0).is_light(a, b))

    def test_is_light3(self):
        a, b = R2Point(0.0, 0.0), R2Point(1.0, 0.0)
        self.assertFalse(R2Point(0.5, 0.5).is_light(a, b))

    def test_is_light4(self):
        a, b = R2Point(0.0, 0.0), R2Point(1.0, 0.0)
        self.assertTrue(R2Point(0.5, -0.5).is_light(a, b))

    # Две точки различны
    def test_eq1(self):
        self.assertNotEqual(R2Point(1.0, 1.0), R2Point(2.0, 2.0))

    # Точка и кортеж отличаются
    def test_eq2(self):
        self.assertNotEqual(R2Point(1.0, 1.0), (1.0, 1.0))

    # Проверка математической функции sign
    def test_sign1(self):
        self.assertEqual(R2Point.sign(-3.5765), -1.0)

    def test_sign2(self):
        self.assertEqual(R2Point.sign(0), 0.0)

    def test_sign3(self):
        self.assertEqual(R2Point.sign(3249.123122), 1.0)

    # Пересикает ли точка круг единичного радиуса
    def test_IWC_point1(self):
        p = R2Point(0.0, 1.0)
        self.assertEqual(p.intersections_with_circle(), 1)

    def test_IWC_point2(self):
        p = R2Point(1.0, 1.0)
        self.assertEqual(p.intersections_with_circle(), 0)

    # Количество пресечений прямой заданой двумя точками
    # пересечений с кругом единичного радиуса
    # через нормальное уравнение прямой
    def test_IWC_line1(self):
        p1 = R2Point(2.0, 1.0)
        p2 = R2Point(1.0, 2.0)
        self.assertEqual(p1.intersections_with_circle(p2), 0)

    def test_IWC_line2(self):
        p1 = R2Point(1.0, 1.0)
        p2 = R2Point(-1.0, 1.0)
        self.assertEqual(p1.intersections_with_circle(p2), 1)

    def test_IWC_line3(self):
        p1 = R2Point(0.0, 0.0)
        p2 = R2Point(1.0, 1.0)
        self.assertEqual(p1.intersections_with_circle(p2), inf)