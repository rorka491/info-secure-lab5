import sys


COMMANDS = "all classics analysis stego hash signature tls incidents tests reports exit".split()
ALIASES = dict(zip("все классика анализ стего хеш подпись tls инциденты тесты отчёты выход".split(),
                   COMMANDS))


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    try:
        from ..providers.app_provider import build_container
        from ..services.report_service import NOTICE, ReportService
    except ImportError as error:
        print(f"Не удалось загрузить зависимость: {error}. Выполните python -m pip install -e .")
        return 1
    print(NOTICE)
    container = build_container()
    try:
        service = container.get(ReportService)
        hint = "Команды: " + ", ".join(COMMANDS)
        if args:
            command = ALIASES.get(args[0], args[0])
            if len(args) != 1 or command not in COMMANDS:
                print(hint)
                return 2
            if command == "exit":
                return 0
            success, output = service.execute(command)
            print(output)
            return 0 if success else 1

        print(hint)
        while True:
            try:
                command = input("CryptoLab> ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                return 0
            command = ALIASES.get(command, command)
            if command == "exit":
                return 0
            if command not in COMMANDS:
                print(hint)
                continue
            _, output = service.execute(command)
            print(output)
    finally:
        container.close()


if __name__ == "__main__":
    raise SystemExit(main())
