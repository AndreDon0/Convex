from deq import Deq
from r2point import R2Point
from adint import Adint


class Figure:
    """ Абстрактная фигура """

    def perimeter(self):
        return 0.0

    def area(self):
        return 0.0

    def IWC(self) -> int:
        return 0


class Void(Figure):
    """ "Hульугольник" """

    def add(self, p):
        return Point(p)


class Point(Figure):
    """ "Одноугольник" """

    def __init__(self, p):
        self.p = p

    def IWC(self) -> int:
        return self.p.intersections_with_circle()

    def add(self, q):
        return self if self.p == q else Segment(self.p, q)


class Segment(Figure):
    """ "Двуугольник" """

    def __init__(self, p, q):
        self.p, self.q = p, q

    def IWC(self) -> int | float:
        return self.q.intersections_with_circle(self.p)

    def perimeter(self):
        return 2.0 * self.p.dist(self.q)

    def add(self, r):
        if R2Point.is_triangle(self.p, self.q, r):
            return Polygon(self.p, self.q, r)
        elif r.is_inside(self.p, self.q):
            return self
        elif self.p.is_inside(r, self.q):
            return Segment(r, self.q)
        else:
            return Segment(self.p, r)


class Polygon(Figure):
    """ Многоугольник """

    def __init__(self, a, b, c):
        self.points = Deq()
        self.points.push_first(b)
        if b.is_light(a, c):
            self.points.push_first(a)
            self.points.push_last(c)
        else:
            self.points.push_last(a)
            self.points.push_first(c)
        self._perimeter = a.dist(b) + b.dist(c) + c.dist(a)
        self._area = abs(R2Point.area(a, b, c))
        self._IWC = Adint(0)
        self._IWC += c.intersections_with_circle(b)
        self._IWC += c.intersections_with_circle(a)
        self._IWC += a.intersections_with_circle(b)

    def perimeter(self):
        return self._perimeter

    def area(self):
        return self._area

    def IWC(self) -> int | float:
        return self._IWC.get()

    # добавление новой точки
    def add(self, t):

        # поиск освещённого ребра
        for n in range(self.points.size()):
            if t.is_light(self.points.last(), self.points.first()):
                break
            self.points.push_last(self.points.pop_first())

        # хотя бы одно освещённое ребро есть
        if t.is_light(self.points.last(), self.points.first()):

            # учёт удаления ребра, соединяющего конец и начало дека
            self._perimeter -= self.points.first().dist(self.points.last())
            self._area += abs(R2Point.area(t,
                                           self.points.last(),
                                           self.points.first()))
            self._IWC -= self.points.last().intersections_with_circle(
                self.points.first())

            # удаление освещённых рёбер из начала дека
            p = self.points.pop_first()
            while t.is_light(p, self.points.first()):
                self._perimeter -= p.dist(self.points.first())
                self._area += abs(R2Point.area(t, p, self.points.first()))
                self._IWC -= p.intersections_with_circle(self.points.first())
                p = self.points.pop_first()
            self.points.push_first(p)

            # удаление освещённых рёбер из конца дека
            p = self.points.pop_last()
            while t.is_light(self.points.last(), p):
                self._perimeter -= p.dist(self.points.last())
                self._area += abs(R2Point.area(t, p, self.points.last()))
                self._IWC -= p.intersections_with_circle(self.points.last())
                p = self.points.pop_last()
            self.points.push_last(p)

            # добавление двух новых рёбер
            self._perimeter += t.dist(self.points.first())
            self._perimeter += t.dist(self.points.last())
            self._IWC += t.intersections_with_circle(self.points.first())
            self._IWC += t.intersections_with_circle(self.points.last())
            self.points.push_first(t)

        return self


if __name__ == "__main__":  # pragma: no cover
    f = Void()
    print(type(f), f.__dict__)
    f = f.add(R2Point(-1, 1))
    print(type(f), f.__dict__)
    f = f.add(R2Point(-1, -1))
    print(type(f), f.__dict__)
    f = f.add(R2Point(2, 2))
    print(type(f), f.__dict__)
    f = f.add(R2Point(2, -2))
    print(type(f), f.__dict__)
