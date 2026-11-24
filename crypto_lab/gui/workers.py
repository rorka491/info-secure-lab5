from PySide6.QtCore import QObject, QRunnable, Signal, Slot


class WorkerSignals(QObject):
    finished = Signal(bool, str)


class ScenarioWorker(QRunnable):
    def __init__(self, service, command):
        super().__init__()
        self.service = service
        self.command = command
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        try:
            success, output = self.service.execute(self.command)
        except Exception as error:
            success, output = False, f"Не удалось выполнить сценарий: {error}"
        self.signals.finished.emit(success, output)
