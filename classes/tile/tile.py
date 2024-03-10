from random import randint
from assets.constants.constants import Constants


__name__ = "tile"
__author__ = "CDL & <votre nom>"
__version__ = 1.0
__license__ = "MIT"


"""
	Classe Tile.
	> Une interface pour une tuile du jeu Sudoku.
"""


class Tile:
    def __init__(self) -> None:
        self._value: int | None = None
        self._hints: set[int] = set()
        self._is_visible: bool = False

    @property
    def value(self) -> int | None:
        return self._value

    @value.setter
    def value(self, value: int | None) -> None:
        self._value = value

    @property
    def hints(self) -> set[int]:
        return self._hints

    @hints.setter
    def hints(self, hints: set[int]) -> None:
        self._hints = hints

    @property
    def is_visible(self) -> bool:
        return self.is_visible

    @is_visible.setter
    def is_visible(self, is_visible: bool) -> None:
        self._is_visible = is_visible

    def switch_visibility(self) -> None:
        """
            Change la visibilité de la tuile.
        """
        self._is_visible = not self._is_visible

    def generate_random_value(self, constraint: set[any] = set()) -> int:
        try:
            constraint = Tile.clean_constraint(constraint)
            assert len(constraint) < Constants.BOARD_SIZE
        except AssertionError:
            print("Error :: generate_random_value :: Invalid constraint.")
            print("Constraint:", constraint)
            return -1

        value: int | None = None

        while value is None or value in constraint:
            value = randint(Constants.MIN_VALUE,
                            Constants.MAX_VALUE)

        return value

    @staticmethod
    def clean_constraint(constraint: set[any]) -> set[int]:
        """
            Nettoie les contraintes pour ne garder que les valeurs.
        """
        return set([value for value in constraint if isinstance(value, int)])
