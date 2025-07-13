from solver import Solver

# TODO Make the 

class CDCL(Solver):
    def __init__(self, clauses:list[list]):
        super().__init__(clauses)

    def solve(self):
        """
        Performs the CDCL algorithm on a list of clauses (lists)
        """
        pass

if __name__ == "__main__":
    clauses = [
        [1, -3, 4],
        [-2, 3],
        [2]
    ]

    model = CDCL(clauses)
    model.solve()
    print(model.results())