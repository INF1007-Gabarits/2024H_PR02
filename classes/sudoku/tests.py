import unittest
import sys
from pathlib import Path
from classes.sudoku.sudoku import Sudoku


project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

__name__ = "tests"
__author__ = "<votre nom>"
__version__ = 1.0


"""
	Tests unitaires pour Sudoku.
	> Testez chacune de vos méthodes de la classe Sudoku.
	> Deux cas de tests par méthode, voir l'énoncé.
"""


class TestSudoku(unittest.TestCase):
    def setUp(self) -> None:
        """
        TODO: Initialiser les ressources avant chaque test.
        """

        self.sudoku = Sudoku()

    def test_generate_empty_board(self):
        """
        TODO: Tester si le tableau vide est généré correctement.
        """

        pass

    def test_complete_board(self):
        """
        TODO: Tester si le tableau est complété correctement.
        """

        pass

    def test_generate_view_board(self):
        """
        TODO: Tester si le plateau de jeu pour l'utilisateur est généré correctement.
        """

        pass


if __name__ == '__main__':
    unittest.main()
