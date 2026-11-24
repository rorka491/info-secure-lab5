import json

from ..domain.certificates import compare_types, inspect_certificate
from ..domain.digital_signature import generate_pair, sign, verify


class SignatureService:
    def run(self, data, artifact_dir=None):
        document = data["documents_for_signing"][0]["text"]
        private, public = generate_pair()
        _, another_public = generate_pair()
        signed = sign(document, private)
        envelope = json.loads(signed.result)
        damaged = bytearray.fromhex(envelope["der"])
        damaged[-1] ^= 1
        altered = json.dumps({**envelope, "der": damaged.hex()})
        if artifact_dir is not None:
            for name, content in (("signed_document.txt", document), ("signature.json", signed.result),
                                  ("public_key.pem", public)):
                (artifact_dir / name).write_text(content, encoding="utf-8")
        params = data["algorithm_params"]
        tls = params["tls"]
        return [signed, verify(document, signed.result, public),
                verify(document + "!", signed.result, public),
                verify(document, signed.result, another_public),
                verify(document, altered, public),
                inspect_certificate(tls["certificate"], tls["server"], tls["as_of"],
                                    tls["trusted_issuer"]),
                compare_types(params["signature_types"])]
