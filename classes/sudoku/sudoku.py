from classes.difficulty.difficulty import Difficulty
import sys
from pathlib import Path


project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

__name__ = "sudoku"
__author__ = "<votre nom>"
__version__ = 1.0


"""
	Classe Sudoku.
	> Une interface pour votre jeu Sudoku.
"""


class Sudoku:
    def __init__(self) -> None:
        self._board = None
        # TODO: Ajoutez vos attributs de classe

    def generate_empty_board(self):
        """
        - TODO: 4.1.1.
        """
        pass

    def complete_board(self):
        """
        - TODO: 4.1.2.
        """
        pass

    def generate_view_board(self):
        """
        - TODO: 4.1.3.
        """
        pass

    # TODO: Ajoutez d'autres méthodes de classe au fil de votre développement, n'oubliez pas de les tester !
