import Simplex
from Simplex import Simplex
 
if __name__ == "__main__":
    """
        MAX fo: 5x + 2y 
        sa:
            2x + y <= 6 
            10x + 12y < = 60
            x, y >= 0

        Forma Simplex:
        z - 5x + 2y = 0
            2x + y + f1 <= 6
            10x + 12y + f2 < = 60
    """
    simplex = Simplex()
    simplex.set_funcao_objetiva([1, -5, -2, 0, 0, 0])
    simplex.add_restricoes([0, 2, 1, 1, 0, 6])
    simplex.add_restricoes([0, 10, 12, 0, 1, 60])

    simplex.resolve()



