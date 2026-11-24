from PySide6.QtWidgets import QPushButton

from .scenario_tab import ScenarioTab


class ReportsTab(ScenarioTab):
    def __init__(self):
        super().__init__("reports", "Открыть итоговый отчёт")
        self.run_all = QPushButton("Сформировать все отчёты")
        self.run_tests = QPushButton("Запустить тесты")
        self.layout().insertWidget(1, self.run_all)
        self.layout().insertWidget(2, self.run_tests)
        self.run_all.clicked.connect(lambda: self.requested.emit("all"))
        self.run_tests.clicked.connect(lambda: self.requested.emit("tests"))
