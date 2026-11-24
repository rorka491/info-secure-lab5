# CryptoLab

CryptoLab is the implementation of the practical part of Cryptography Lab 5. It runs scripted experiments against fictional inputs and generates reports. The optional classical exercise uses a teaching rotor.

## Install and run

Use Python 3.10 or newer. Run these commands from the directory containing this README and `pyproject.toml`.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e .
.\.venv\Scripts\python.exe -m crypto_lab.cli.main all
.\.venv\Scripts\python.exe -m crypto_lab.gui.app
.\.venv\Scripts\python.exe -m pytest -q crypto_lab/tests
```

With the environment activated, use `python -m crypto_lab.cli.main all` and `python -m crypto_lab.gui.app`. On Linux and macOS the environment executable is `.venv/bin/python`.

The CLI accepts `all`, `classics`, `analysis`, `stego`, `hash`, `signature`, `tls`, `incidents`, `tests`, `reports` and `exit`. Run it without arguments for an interactive prompt. The GUI runs the same scenarios in background workers. Use the Reports tab to run the complete workflow or the test suite.

`all` generates the reports in `reports/` relative to the working directory. It also saves the sample document, its signature envelope and the public key for verification. Cryptographic artifacts change on each run because the scenarios use fresh keys. The checked-in reports document a completed run.

## Structure

- `crypto_lab/domain` implements transformations and returns structured results.
- `crypto_lab/data` contains fictional data, algorithm parameters and the JSON repository.
- `crypto_lab/services` runs experiments and generates reports.
- `crypto_lab/providers` binds paths, repositories and services through Dishka.
- `crypto_lab/cli` and `crypto_lab/gui` call the same service.
- `crypto_lab/tests` covers normal cases, malformed inputs and deliberate modifications.
- `crypto_lab/docs` contains algorithm notes, the experiment protocol, case studies and answers.

# info-secure-lab5
