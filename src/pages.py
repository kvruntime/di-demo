from PyQt6.QtWidgets import *

from viewmodels import HomeViewModel, UserViewModel


class HomePage(QWidget):
    def __init__(self, vm: HomeViewModel, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.resize(400, 400)

        self.vm = vm

        layout = QVBoxLayout(self)

        self.label = QLabel("Service")
        self.buttonCaller = QPushButton("Caller")

        layout.addWidget(QLabel("HomePage"))
        layout.addWidget(self.label)
        layout.addWidget(self.buttonCaller)

        self.initializeBinding()
        return

    def initializeBinding(self) -> None:
        self.buttonCaller.clicked.connect(self.vm.command_operation)
        self.label.setText(f"Data: {self.vm.sdata}")
        return None


class UserPage(QWidget):
    def __init__(self, vm: UserViewModel, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.resize(400, 400)

        self.vm = vm

        layout = QVBoxLayout(self)

        self.label = QLabel("Service")
        self.buttonCaller = QPushButton("Caller")

        layout.addWidget(QLabel("UserPage"))
        layout.addWidget(self.label)
        layout.addWidget(self.buttonCaller)

        self.initializeBinding()
        return

    def initializeBinding(self) -> None:
        self.buttonCaller.clicked.connect(self.vm.command_operation)
        self.label.setText(f"Data: {self.vm.sdata}")
        return None
