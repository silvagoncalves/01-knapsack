import os


class KnapsackInstance:
    """

    >>> data = KnapsackInstance.test_instance()
    >>> kp = KnapsackInstance.from_string(data)
    >>> kp
    KnapsackInstance(W=[13, 13, 13, 10, 24, 11], V=[2600, 2600, 2600, 500, 4500, 960], C=50)

    >>>

    """

    @staticmethod
    def from_string(string: str) -> "KnapsackInstance":
        """ """
        W: list[int] = []
        V: list[int] = []
        C: int = 0

        return KnapsackInstance(W, V, C)

    @staticmethod
    def load_instance_data(instance_name: str) -> str:
        return ''

    @staticmethod
    def test_instance() -> str:
        test_data = (
            "6 50",
            "13 2600",
            "13 2600",
            "13 2600",
            "10 500",
            "24 4500",
            "11 960",
        )
        return "\n".join(test_data)

    def __init__(self, W: list[int], V: list[int], C: int) -> None:
        self.W: list[int] = W
        self.V: list[int] = V
        self.C: int = C
        self.size: int = len(W)

    def __repr__(self):
        return f"{__class__.__name__}(W={self.W}, V={self.V}, C={self.C})"


class KnapsackSolver:
    """
    General abstract solver for 01-Knapsack problem

    >>> kp = KnapsackInstance(W=[13, 13, 13, 10, 24, 11], V=[2600, 2600, 2600, 500, 4500, 960], C=50)

    >>> s = KnapsackSolver(kp)
    >>> s.weight(X=[1, 1, 1, 1, 1, 1])
    84
    """

    def __init__(self, instance) -> None:
        self._inst = instance
        # 0-1 decision variables
        self._X: list[int] = [0] * self._inst.size

    def solve(self) -> tuple[int, ...]:
        """
        Solves the loaded instance and returns the assignment to the decision
        variables
        """
        items = [
            (i, self._inst.V[i], self._inst.W[i], self._inst.V[i] / self._inst.W[i])
            for i in range(self._inst.size)
        ]
        raise NotImplementedError

    def weight(self, X: tuple[int, ...]) -> int:
        """
        Computes the total volume of the objects contained in the solution X
        """
        return sum(w * x for w, x in zip(self._inst.W, X))

    def value(self, X: tuple[int, ...]) -> int:
        """
        Computes the total value of the objects contained in the solution X
        """
        return sum(v * x for v, x in zip(self._inst.V, X))


try:
    import doctest

    doctest.testmod()
except:
    print("Unable to load doctests")
