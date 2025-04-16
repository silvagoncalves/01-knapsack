# Exercice https://courses.21-learning.com/runestone/books/published/oci-2224-donc/classic-problems/01-knapsack-short.html#force-brute

from knapsack import KnapsackInstance, KnapsackSolver

class BruteforceKnapsackSolver(KnapsackSolver):
    """
    >>> kp = KnapsackInstance(W=[13, 13, 13, 10, 24, 11], V=[2600, 2600, 2600, 500, 4500, 960], C=50)
    >>> bfs = BruteforceKnapsackSolver(kp)
    >>> Xopt = bfs.solve()
    >>> Xopt in [(0, 1, 1, 0, 1, 0), (1, 0, 1, 0, 1, 0), (1, 1, 0, 0, 1, 0)]
    True
    >>> bfs.value(Xopt)
    9700
    >>> bfs.weight(Xopt)
    50
    >>> bfs.weight(Xopt) <= bfs._inst.C
    True

    """
    
    def __init__(self, instance) -> None:
        # TODO: write the constructor by calling the parent class constructor
        super().__init__(instance)

    
    def solve(self) -> tuple[int, ...]:
        # solve by brute force
        n = len(self._inst.W)
        best_val = 0
        best_sol = tuple(0 for _ in range(n))

        for comb in product([0, 1], repeat=n):
            total_weight = sum(w * x for w, x in zip(self._inst.W, comb))
            if total_weight <= self._inst.C:
                total_value = sum(v * x for v, x in zip(self._inst.V, comb))
                if total_value > best_val:
                    best_val = total_value
                    best_sol = comb

        return best_sol