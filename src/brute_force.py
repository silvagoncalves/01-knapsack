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
        # Cette méthode retourne une solution optimale au problème du sac à dos par force brute

        n = len(self._inst.W)  # Nombre total d’objets

        best_val = 0  # Meilleure valeur trouvée jusqu’à présent
        best_sol = tuple(0 for _ in range(n))  # Meilleure solution trouvée (initialement : ne rien prendre)

        # Génère toutes les combinaisons possibles de 0 et 1 (ne pas prendre / prendre chaque objet)
        # Exemple : pour 3 objets → (0,0,0), (0,0,1), ..., (1,1,1)
        for comb in product([0, 1], repeat=n):
            # Calcule le poids total de cette combinaison
            total_weight = sum(w * x for w, x in zip(self._inst.W, comb))

            # Vérifie si ce poids ne dépasse pas la capacité du sac
            if total_weight <= self._inst.C:
                # Calcule la valeur totale (kcal) de cette combinaison
                total_value = sum(v * x for v, x in zip(self._inst.V, comb))

                # Si cette combinaison est meilleure que les précédentes, on la garde
                if total_value > best_val:
                    best_val = total_value      # Nouvelle meilleure valeur
                    best_sol = comb             # Nouvelle meilleure combinaison d’objets

        # Retourne la meilleure combinaison trouvée (par exemple : (1, 1, 0, 0, 1, 0))
        return best_sol