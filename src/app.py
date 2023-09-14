import sys
from di_builder import di

from pages import HomePage
from PyQt6.QtWidgets import QApplication
from services import DataService

from viewmodels import HomeViewModel

di.add_singleton(HomePage)


class Application(QApplication):
    def __init__(self) -> None:
        super().__init__([])
        self.page = di.resolve(HomePage)
        return


    def run(self) -> None:
        self.page.show()
        sys.exit(self.exec())



di.add_singleton(Application)
