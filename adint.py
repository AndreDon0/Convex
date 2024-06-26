from math import inf


class Adint:

    def __init__(self, x: int | float) -> None:
        if x == inf:
            self.x = 0
            self.INF = 1
        else:
            self.x = x
            self.INF = 0

    def __add__(self, other: int | float):
        if other == inf:
            self.INF += 1
        else:
            self.x += other
        return self

    def __sub__(self, other: int | float):
        if other == inf:
            self.INF -= 1
        else:
            self.x -= other
        return self

    def get(self) -> int | float:
        return inf if self.INF > 0 else self.x

    def __repr__(self) -> str:
        return str(inf) if self.INF > 0 else str(self.x)


if __name__ == "__main__":  # pragma: no cover
    a = Adint(3)
    print(a)
    a += inf
    print(a)
    a += 9
    print(a)
    a -= inf
    print(a)
