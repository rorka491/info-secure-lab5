from PySide6.QtCore import QThreadPool, Slot
from PySide6.QtWidgets import QLabel, QMainWindow, QTabWidget, QVBoxLayout, QWidget

from ..services.report_service import NOTICE, TITLES
from .tabs.analysis_tab import AnalysisTab
from .tabs.classics_tab import ClassicsTab
from .tabs.hash_tab import HashTab
from .tabs.incidents_tab import IncidentsTab
from .tabs.reports_tab import ReportsTab
from .tabs.signature_tab import SignatureTab
from .tabs.stego_tab import StegoTab
from .tabs.tls_tab import TlsTab
from .workers import ScenarioWorker


class MainWindow(QMainWindow):
    def __init__(self, service):
        super().__init__()
        self.service = service
        self.pool = QThreadPool(self)
        self.worker = None
        self.active_tab = None
        self.setWindowTitle("CryptoLab · Лабораторная работа № 5")
        self.resize(980, 680)
        self.tabs = QTabWidget()
        root = QWidget()
        layout = QVBoxLayout(root)
        notice = QLabel(NOTICE)
        notice.setWordWrap(True)
        layout.addWidget(notice)
        layout.addWidget(self.tabs)
        self.setCentralWidget(root)

        for tab_type in (ClassicsTab, AnalysisTab, StegoTab, HashTab,
                         SignatureTab, TlsTab, IncidentsTab, ReportsTab):
            tab = tab_type()
            tab.requested.connect(self.start)
            self.tabs.addTab(tab, TITLES[tab.command])

    @Slot(str)
    def start(self, command):
        if self.worker is not None:
            return
        self.active_tab = self.tabs.currentWidget()
        self.active_tab.status.setText("Сценарий выполняется…")
        self.tabs.setEnabled(False)
        self.worker = ScenarioWorker(self.service, command)
        self.worker.signals.finished.connect(self.finish)
        self.pool.start(self.worker)

    @Slot(bool, str)
    def finish(self, success, output):
        self.active_tab.show_result(success, output)
        self.worker = None
        self.tabs.setEnabled(True)

    def closeEvent(self, event):
        if self.worker is not None:
            self.active_tab.status.setText("Дождитесь завершения запущенного сценария.")
            event.ignore()
            return
        super().closeEvent(event)
