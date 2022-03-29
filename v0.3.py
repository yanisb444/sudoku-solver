import numpy as np


class GrilleSudoku:
    #  Classe qui prend en parametre la grille ainsi que la taille de son cote (ici 9x9)
    def __init__(self, grille, taille_grille):
        self.grille = grille
        self.taille = taille_grille

    def IsPresentInCol(self, col, num):
        """Verify if 'num' is in 'col'."""
        for row in self.grille:
            if self.grille[row, col] == num:
                return True
        return False

    def IsPresentInRow(self, row, num ):
        """Verify if 'num' is in 'row'."""
        for col in range(9):
            if self.grille[row, col] == num :
                return True
        return False

    def IsPresentInGrid(self, boxStartRow, boxStartCol, num):
        """Verify if 'num' is in a sub-grid."""
        for row in range(boxStartRow, boxStartRow+2):
            for col in range(boxStartCol, boxStartCol+2):
                if self.grille[row, col] == num :
                    return True
        return False

    def __repr__(self):
        """Definition d'une nouvelle grille de Sudoku entree par l'User"""
        return str(self.grille)


"""
def create_grid(puzzle_str):
    #  Deleting whitespaces and newlines (\n)
    lines = puzzle_str.replace(' ', '').replace('\n', '')
    # Converting it to a list of digits
    digits = list(map(int, lines))
    # Turning it to a 9x9 numpy array
    grid = np.array(digits).reshape(9, 9)
    return grid


def create_puzzle_str() -> list:
    grid = []
    #  Inputting the grid line by line
    for k in range(9):
        line = input(f"Enter the N°{k+1} line : ")
        grid.append(line)
    #  Returning the grid on NumPy format
        grid = np.array(grid).reshape(9,9)
    return grid
"""

#  Resolve the Sudoku

# Print the result

# Main program

tailleGrille = 9

grilleUser = [[2, 0, 8, 3, 0, 0, 7, 0, 0],
              [4, 9, 0, 1, 5, 7, 0, 0, 2],
              [0, 0, 3, 0, 0, 4, 1, 9, 0],
              [1, 8, 5, 0, 6, 0, 0, 2, 0],
              [0, 0, 0, 0, 2, 0, 5, 6, 0],
              [9, 6, 0, 4, 0, 5, 3, 0, 0],
              [0, 3, 0, 0, 7, 2, 0, 0, 4],
              [0, 4, 9, 0, 3, 0, 0, 5, 7],
              [8, 2, 7, 0, 0, 9, 0, 1, 3]]
grilleUser = np.array(grilleUser).reshape(9, 9)

Sudoku = GrilleSudoku(grilleUser, 9)

print("Grid shape : \n", Sudoku.grille.shape)
print("Grid size : \n", Sudoku.grille.size)
