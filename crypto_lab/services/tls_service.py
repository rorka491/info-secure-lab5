from ..domain.tls_model import simulate


class TlsService:
    def run(self, data):
        return [simulate(data["messages"][0]["text"], data["algorithm_params"]["tls"])]
