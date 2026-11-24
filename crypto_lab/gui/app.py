def main():
    try:
        from PySide6.QtWidgets import QApplication

        from ..providers.app_provider import build_container
        from ..services.report_service import ReportService
        from .main_window import MainWindow
    except ImportError as error:
        print(f"Не удалось загрузить зависимость: {error}. Выполните python -m pip install -e .")
        return 1

    app = QApplication([])
    container = build_container()
    try:
        window = MainWindow(container.get(ReportService))
        window.show()
        return app.exec()
    finally:
        container.close()


if __name__ == "__main__":
    raise SystemExit(main())
