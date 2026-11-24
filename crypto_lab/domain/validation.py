from functools import wraps

from .contracts import CryptoResult


def require(condition, message):
    if not condition:
        raise ValueError(message)


def require_text(value):
    require(isinstance(value, str) and bool(value.strip()), "Введите непустой текст.")


def checked(algorithm):
    def decorate(function):
        @wraps(function)
        def run(source, *args, **kwargs):
            try:
                return function(source, *args, **kwargs)
            except (ValueError, TypeError, KeyError, AttributeError) as error:
                message = (str(error) if isinstance(error, ValueError) else
                           "Несовместимые параметры или отсутствуют обязательные поля.")
                return CryptoResult(
                    algorithm, function.__name__, source if isinstance(source, str) else "",
                    status="error", explanation=message,
                )
        return run
    return decorate
