# Base solver class

class Solver:
    def __init__(self, clauses:list[list]):
        if not clauses:
            raise ValueError("No clauses provided. At least one clause is required.")
        
        self.clauses = clauses
        self.solved = False

    # ---------------------------------Solver-----------------------
    def solve(self):
        """
        Create the solve function here
        Make sure to return the satisfiability result and solved to True
        """
        raise NotImplementedError("Subclasses must implement the solve method")
    
    # ---------------prints------------------
    def results(self):
        """
        Get the satisfiability result.
        
        Returns:
            bool: True if the formula is satisfiable, False if unsatisfiable.
            
        Raises:
            RuntimeError: If solve() has not been called yet.
        """
        if self.solved:
            return self.satisfiable
        else:
            raise RuntimeError("Solver not activated yet. Call solve() first.")