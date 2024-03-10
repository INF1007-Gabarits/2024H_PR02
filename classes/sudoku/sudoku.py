from assets.constants.constants import Constants
from classes.tile.tile import Tile
import sys
from pathlib import Path
from math import sqrt
from random import choice


project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

__name__ = "sudoku"
__author__ = "CDL & <votre nom>"
__version__ = 1.0
__license__ = "MIT"


"""
	Classe Sudoku.
	> Une interface pour votre jeu Sudoku.
"""


class Sudoku:
    def __init__(self) -> None:
        self._board: list[list[Tile]] = self.init_board()

    def init_board(self) -> list[list[Tile]]:
        """
                                                                                                                                                                                                                                                                        Initialise le plateau de jeu.
        """
        return [[Tile() for _ in range(Constants.BOARD_SIZE)] for _ in range(Constants.BOARD_SIZE)]

    def get_tile(self, row: int, col: int) -> Tile:
        """
                                                                                                                                                                                                                                                                        Retourne la tuile à la position (row, col).
        """
        try:
            return self._board[row][col]
        except IndexError:
            print("Error :: get_tile :: Invalid position.")
            return Tile()

    def get_row_tiles(self, row: int) -> list[Tile]:
        """
                                                                                                                                                                                                                                                                        Retourne toutes les tuiles de la rangée row.
        """
        try:
            return self._board[row]
        except IndexError:
            print("Error :: get_row_tiles :: Invalid row.")
            return []

    def get_col_tiles(self, col: int) -> list[Tile]:
        """
                                                                                                                                                                                                                                                                        Retourne toutes les tuiles de la colonne col.
        """
        try:
            return [self._board[row][col] for row in range(Constants.BOARD_SIZE)]
        except IndexError:
            print("Error :: get_col_tiles :: Invalid col.")
            return []

    def get_square_tiles(self, row: int, col: int) -> list[Tile]:
        """
                                                                                                                                                                                                                                                                        Retourne toutes les tuiles de la sous-grille à la position (row, col).
        """
        squared_root_board_size = int(sqrt(Constants.BOARD_SIZE))
        try:
            square_row = row // squared_root_board_size
            square_col = col // squared_root_board_size
            return [self._board[square_row * squared_root_board_size + i][square_col * squared_root_board_size + j] for i in range(squared_root_board_size) for j in range(squared_root_board_size)]
        except IndexError:
            print("Error :: get_square_tiles :: Invalid position.")
            return []

    def is_valid_move(self, row: int, col: int, value: int) -> bool:
        """
                                                                                                                                                                                                                                                                        Vérifie si la valeur value peut être placée à la position (row, col).
        """
        return value not in [tile.value for tile in self.get_row_tiles(row)] and value not in [tile.value for tile in self.get_col_tiles(col)] and value not in [tile.value for tile in self.get_square_tiles(row, col)]

    def get_missing_values_positions(self) -> set[tuple[int, int]]:
        """
                                                                                                                                                                                                                                                                        Retourne toutes les positions des tuiles vides.
        """
        missing_value_positions: set[tuple[int, int]] = set()

        for i in range(Constants.BOARD_SIZE):
            for j in range(Constants.BOARD_SIZE):
                if self.get_tile(i, j).value is None:
                    missing_value_positions.add((i, j))

        return missing_value_positions

    def populate_board(self) -> None:
        """
                                                                                                                                        Remplit le plateau de jeu.
        """
        while True:
            missing_value_positions: set[tuple[int, int]
                                         ] = self.get_missing_values_positions()
            if not missing_value_positions:
                break

            row, col = choice(list(missing_value_positions))

            constraint = set([tile.value for tile in self.get_row_tiles(
                row)] + [tile.value for tile in self.get_col_tiles(col)] + [tile.value for tile in self.get_square_tiles(row, col)])

            if len(constraint) >= Constants.BOARD_SIZE:
                continue

            self.get_tile(row, col).value = self.get_tile(
                row, col).generate_random_value(constraint)

    def print_board(self) -> None:
        """
                                                                        Affiche le plateau de jeu.
        """
        for i in range(Constants.BOARD_SIZE):
            for j in range(Constants.BOARD_SIZE):
                print(self.get_tile(i, j).value, end=" ")
            print()


sudoku: Sudoku = Sudoku()

sudoku.populate_board()

sudoku.print_board()

print(sudoku.get_missing_values_positions())
