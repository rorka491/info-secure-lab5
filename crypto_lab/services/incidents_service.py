from ..domain.incidents import inspect_log, summarize


class IncidentsService:
    def run(self, data):
        params = data["algorithm_params"]
        return [summarize(params["incidents"]),
                inspect_log(data["test_scenarios"]["journal"], params["network"])]
