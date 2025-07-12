# I want to start the DPLL algorithmn here
# https://en.wikipedia.org/wiki/DPLL_algorithm

# TODO Unit propagation - IF there is only choce for a clause, do it
# TODO Pure Literal Elimination - Elimiating clauses that have no effect on the rest of the system

def DPLL(clauses:list) -> bool:
    """
    Perfroms the DPLL algorithm on a list of clauses
    returns True is satisfiable, False if otherwise
    """

    # Unit progpagation
    while any(len(clause) == 1 for clause in clauses):
        for i in range(len(clauses)):
            if range(len(clauses[i])) == 1:
                pass

    # Pure Literal Elimination
    for pure_literal in clauses:
        # TODO implement pure literal elimation
        pass

    # Stopping Conditions
    if not clauses:
        # If clauses is empty return True
        return True
    
    if False:
        # if there is an empty clause
        return False
    
    # Continue DPLL
    l = clauses[0] # Choose a literal 
    # Return DPLL(clauses and +l) or DPLL(clause and -1)

if __name__ == "__main__":

    clauses = [
    [1, -3, 4],   # (x1 OR NOT x3 OR x4)
    [-2, 3],      # (NOT x2 OR x3)
    [2]           # (x2)
    ]

    print(DPLL(clauses))