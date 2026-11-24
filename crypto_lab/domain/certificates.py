from datetime import date
import json

from .contracts import CryptoResult
from .validation import checked, require


@checked("certificate")
def inspect_certificate(card, server, as_of, trusted_issuer):
    fields = {"subject", "issuer", "valid_from", "valid_until", "serial", "purpose", "status"}
    require(isinstance(card, dict) and fields <= card.keys(), "Карточка сертификата неполная.")
    active = date.fromisoformat(card["valid_from"]) <= date.fromisoformat(as_of) <= date.fromisoformat(
        card["valid_until"])
    trusted = (active and card["subject"] == server and card["issuer"] == trusted_issuer
               and card["purpose"] == "server" and card["status"] == "active")
    return CryptoResult("certificate", "inspect", server, json.dumps(card, ensure_ascii=False),
                        status="ok" if trusted else "error",
                        explanation="Условная проверка карточки пройдена." if trusted else
                        "Условная проверка сервера, издателя, срока или назначения отклонена.")


@checked("signature_types")
def compare_types(rows):
    require(isinstance(rows, list) and len(rows) == 3, "Ожидаются три вида подписи.")
    return CryptoResult("signature_types", "compare", "63-ФЗ",
                        json.dumps(rows, ensure_ascii=False, indent=2),
                        explanation="Не является юридически значимой УКЭП.")
