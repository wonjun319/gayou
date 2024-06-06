from .errors import error_handler
from requests import Response
from typing import Any
import requests

@error_handler
def _call_get(url: str, **kwargs: Any) -> Response:
    return requests.get(url, **kwargs)