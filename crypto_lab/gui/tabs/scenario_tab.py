from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLabel, QPlainTextEdit, QPushButton, QVBoxLayout, QWidget


class ScenarioTab(QWidget):
    requested = Signal(str)

    def __init__(self, command, button_text="Выполнить сценарий"):
        super().__init__()
        self.command = command
        self.run_button = QPushButton(button_text)
        self.status = QLabel()
        self.output = QPlainTextEdit(readOnly=True)
        layout = QVBoxLayout(self)
        layout.addWidget(self.run_button)
        layout.addWidget(self.status)
        layout.addWidget(self.output)
        self.run_button.clicked.connect(lambda: self.requested.emit(self.command))

    def show_result(self, success, content):
        self.output.setPlainText(content)
        self.status.setText("Готово" if success else "Сценарий завершился с ошибкой")
