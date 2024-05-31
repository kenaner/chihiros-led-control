"""CII RGB device Model."""

from .base_device import BaseDevice


class C2RGB(BaseDevice):
    """Chihiros CII RGB device Class."""

    _model_name = "CII RGB"
    _model_codes = ["DYNCRGP"]
    _colors: dict[str, int] = {
        # TODO validate that
        # "white": 0,
        "red": 0,
        "green": 1,
        "blue": 2,
    }
