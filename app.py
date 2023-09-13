from di_builder import di

from pages import HomePage
from PyQt6.QtWidgets import QApplication
from services import DataService

from viewmodels import HomeViewModel

di.add_singleton(HomePage)


class Application(QApplication):
    def __init__(self) -> None:
        super().__init__([])
        # self.register()

        self.page = di.resolve(HomePage)
        return

    def register(self):
        di.add_singleton(HomePage)
        di.add_singleton(HomeViewModel)
        di.add_singleton(DataService)
        di.add_singleton(self.__class__)
        return None

    def run(self) -> None:
        self.page.show()
        self.exec()
        return


di.add_singleton(Application)
