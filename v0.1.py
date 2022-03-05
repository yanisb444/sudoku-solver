# Apprehend entree
def new_sudoku():
    """Definition d\'une nouvelle grille de Sudoku entree par l\'User"""
    grille = []
    ligne = []
    for k in range(9):  # grille en 9x9

        while True:  # La boucle continue tant que la ligne n'est pas conform
            ligne = []

            ligne = list(input(f'Entrez la ligne N°{k + 1} (les cases videos = 0) :'))
            if test_line_sudoku(ligne):
                break
        grille[k] = ligne

    return grille


def test_line_sudoku(line_loc):
    """Verifie si l'entree USER est bien conforme aux regles du Sudoku"""
    if len(line_loc) == 9:  # Retour si LONGUEUR de la ligne INCORRECTE
        print("ENTREE INCORRECTE : La grille a un format de 9x9 !")
        return False

    for n in line_loc:  # Verifie si tous les elements de la liste sont des nombres
        print(n)
        if type(n) != int:  # Retour si TYPE de n INCORRECTE
            print("ENTREE INCORRECTE : Une des cases de votre ligne n'est pas un chiffre")
            return False

    return True
# Verify if the entry is okay

# Resolve the Sudoku

# Print the result
