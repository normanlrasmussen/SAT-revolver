# I want to start the DPLL algorithmn here
# https://en.wikipedia.org/wiki/DPLL_algorithm

# TODO Unit propagation - IF there is only choce for a clause, do it
# TODO Pure Literal Elimination - Elimiating clauses that have no effect on the rest of the system

class DPLL:
    def __init__(self, clauses:list[list]):
        if not clauses:
            raise ValueError("No Clauses given")
        
        self.clauses = clauses
        self.solved = False

    # -------------------Helper Functions----------------------------
    def update_clauses(self, clauses:list, literal:int):
        """
        Takes in clauses and literal and removes litereal from clauses
        """
        
        new_clauses = []
        for clause in clauses:
            if literal in clause:
                # Clause is satisfied, so remove it
                continue
            elif -literal in clause:
                # Remove the negated literal from clause
                new_clause = [l for l in clause if l != -literal]
                if not new_clause:
                    # Conflict: empty clause created
                    return None
                new_clauses.append(new_clause)
            else:
                # Clause unchanged
                new_clauses.append(clause)
        return new_clauses
    
    def unit_propagate(self, clauses:list, assignment:dict):
        """
        Perform unit propagation on clauses (list of lists).
        Returns (updated_clauses, updated_assignment).
        """

        changed = True
        while changed:
            changed = False
            # Find all unit clauses
            unit_clauses = [c[0] for c in clauses if len(c) == 1]
            if not unit_clauses:
                break
            # Pick one unit clause to propagate
            unit = unit_clauses[0]
            assignment[abs(unit)] = unit > 0

            clauses = self.update_clauses(clauses, unit)
            if clauses is None:
                return None, None
            changed = True  # Since we modified the formula, check for more unit clauses

        return clauses, assignment

    def pure_literal_elimination(self, clauses:list, assignment:dict):
        """
        Perform pure literal elimination on clauses (list of lists).
        Returns (updated_clauses, updated_assignment).
        """

        changed = True
        while changed:
            changed = False
            # Find all pure litereals
            all_literals = set([literal for clause in clauses for literal in clause])
            
            pure_literal = None
            for literal in all_literals:
                if -literal not in all_literals:
                    pure_literal = literal
                    break
            
            if pure_literal is None:
                break
            
            assignment[abs(pure_literal)] = pure_literal > 0

            clauses = [clause for clause in clauses if pure_literal not in clause]

            changed = True  # Since we modified the formula, check for more pure literals

        return clauses, assignment

    # ---------------------------------Solver-----------------------
    def solve(self):
        """
        Perfroms the DPLL algorithm on a list of clauses (lists)
        returns True is satisfiable, False if otherwise
        """
        clauses = self.clauses
        assignments = {}

        self.satisfiable = self.recursive_solve(clauses, assignments)
        self.solved = True


    def recursive_solve(self, clauses:list, assignments:dict):  
        """
        Perfroms the DPLL algorithm on a list of clauses (lists)
        returns True is satisfiable, False if otherwise
        """
        

        # Unit progpagation
        clauses, assignments = self.unit_propagate(clauses, assignments)
        if not clauses and not assignments:
            return False
                        
        # Pure Literal Elimination
        clauses, assignments = self.pure_literal_elimination(clauses, assignments)

        # Stopping Conditions
        if not clauses:
            # If clauses is empty return True
            return True
        
        # Continue DPLL
        literal = clauses[0][0] # Choose a literal 
        
        yes_literal_clauses = self.update_clauses(clauses, literal)
        if yes_literal_clauses is None:
            yes_bool = False
        else:
            yes_bool = self.recursive_solve(yes_literal_clauses, assignments)
        
        no_literal_clauses = self.update_clauses(clauses, literal)
        if no_literal_clauses is None:
            no_bool = False
        else:
            no_bool = self.recursive_solve(no_literal_clauses, assignments)


        return yes_bool or no_bool
    
    # ---------------prints------------------
    def results(self):
        if self.solved:
            return self.satisfiable
        else:
            raise RuntimeError("Solver not activated yet")


if __name__ == "__main__":

    clauses = [
    [1, -3, 4],   # (x1 OR NOT x3 OR x4)
    [-2, 3],      # (NOT x2 OR x3)
    [2]           # (x2)
    ]

    model = DPLL(clauses)
    model.solve()
    print(model.results())