"""
TODO 4.4. Journalisation
- Ce fichier est fourni à titre d'exemple. 
- Vous pouvez le modifier à votre guise.
- Une seule instance de Logger doit être utilisée dans 
  tout le projet (SingletonType).
- Si vous souhaitez avoir d'autres classes Singleton, 
  vous pouvez déplacer 'SingletonType' au sein d'un fichier dédié.
"""


import logging
from logging.handlers import RotatingFileHandler


__name__ = "logger"
__author__ = "CDL & <votre nom>"
__version__ = 1.0


class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=SingletonType):
    def __init__(self):
        self.log_format = "%(asctime)s - %(levelname)s - %(message)s"
        self.date_format = "%Y-%m-%d %H:%M:%S"
        logging.basicConfig(level=logging.DEBUG,
                            format=self.log_format, datefmt=self.date_format)
        self.log_file = "XXX.log"
        self.file_handler = RotatingFileHandler(
            self.log_file, maxBytes=5*1024*1024, backupCount=2)
        self.file_handler.setLevel(logging.DEBUG)
        self.file_handler.setFormatter(logging.Formatter(
            self.log_format, datefmt=self.date_format))
        self.logger = logging.getLogger('')
        self.logger.addHandler(self.file_handler)

        # TODO: Ajoutez d'autres attributs de classe si nécessaire

    def log(self, message, level):
        # TODO: À refactoriser à l'aide de votre interface 'Difficulty'
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'critical':
            self.logger.critical(message)

        # TODO: Ajoutez d'autres méthodes de classe si nécessaire


# Exemple d'utilisation
logger1 = Logger()
logger2 = Logger()

# Retourne vrai, logger1 and logger2 réfèrent vers la même instance (en raison de 'SingletonType')
print(logger1 == logger2)

# Exemples de journalisation
logger1.log("This is an informational message.", "info")
logger1.log("This is a debug message.", "debug")
logger1.log("This is a critical message.", "critical")
