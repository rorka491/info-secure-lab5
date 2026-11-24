from dataclasses import dataclass
from pathlib import Path

from dishka import Provider, Scope, make_container, provide

from ..data.repository import Repository
from ..services.analysis_service import AnalysisService
from ..services.crypto_service import CryptoService
from ..services.incidents_service import IncidentsService
from ..services.integrity_service import IntegrityService
from ..services.report_service import ReportService
from ..services.signature_service import SignatureService
from ..services.stego_service import StegoService
from ..services.tls_service import TlsService


@dataclass(frozen=True)
class Paths:
    package: Path
    data: Path
    tests: Path
    reports: Path


class AppProvider(Provider):
    scope = Scope.APP
    crypto = provide(CryptoService)
    analysis = provide(AnalysisService)
    stego = provide(StegoService)
    integrity = provide(IntegrityService)
    signature = provide(SignatureService)
    tls = provide(TlsService)
    incidents = provide(IncidentsService)

    @provide
    def paths(self) -> Paths:
        package = Path(__file__).resolve().parents[1]
        return Paths(package, package / "data", package / "tests", Path.cwd() / "reports")

    @provide
    def repository(self, paths: Paths) -> Repository:
        return Repository(paths.data)

    @provide
    def report_service(self, repo: Repository, paths: Paths, crypto: CryptoService,
                       analysis: AnalysisService, stego: StegoService, integrity: IntegrityService,
                       signature: SignatureService, tls: TlsService,
                       incidents: IncidentsService) -> ReportService:
        return ReportService(repo, paths, {
            "classics": crypto, "analysis": analysis, "stego": stego, "hash": integrity,
            "signature": signature, "tls": tls, "incidents": incidents,
        })


def build_container():
    return make_container(AppProvider())
