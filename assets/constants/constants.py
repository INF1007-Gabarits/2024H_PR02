__name__ = "constants"
__author__ = "<votre nom>"
__version__ = 1.0


"""
	Classe Constants.
	> Une interface pour toutes les constantes utilisées dans le cadre de ce projet.
"""


class Constants:
    ASSETS_IMAGES: str = 'assets/images/'
    ASSETS_SOUNDS: str = 'assets/sounds/'
    BOARD_SIZE: int = 9
    MAX_VALUE: int = 9
    MIN_VALUE: int = 1
    SCREEN_WIDTH: int = 800
    SCREEN_HEIGHT: int = 600
    BUTTON_SPACING: int = 20
    BUTTON_WIDTH: int = 60
    BUTTON_HEIGHT: int = 30
    GAME_TITLE: str = "Sudoku"
    SPLASH_SCREEN_BACKGROUND: str = ASSETS_IMAGES + 'splash-bg.jpg'
    SUDOKU_SCREEN_BACKGROUND: str = ASSETS_IMAGES + 'sudoku-bg.jpg'
    PLAY_BUTTON: str = ASSETS_IMAGES + 'play-btn.png'
    REFRESH_BUTTON: str = ASSETS_IMAGES + 'refresh-btn.png'
    HINT_BUTTON: str = ASSETS_IMAGES + 'hint-btn.png'
    FAVICON: str = ASSETS_IMAGES + 'favicon.png'
    MUSIC_PATH: str = ASSETS_SOUNDS + 'music.mp3'
    DEFAULT_VOLUME: float = 0.3
    # TODO: Ajouter d'autres constantes utiles pour le projet.
