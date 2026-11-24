from dataclasses import dataclass, field


@dataclass(frozen=True)
class CryptoResult:
    algorithm: str
    operation: str
    source_message: str
    result: str = ""
    key_or_params: dict = field(default_factory=dict)
    status: str = "ok"
    explanation: str = ""
