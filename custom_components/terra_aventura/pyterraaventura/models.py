"""Models used by PyTerraAventura."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class TerraAventuraLoginCurrentUser:
    """TerraAventura Login Current User."""

    uid: str
    name: str


@dataclass
class TerraAventuraLoginResponse:
    """TerraAventura Login Response."""

    current_user: TerraAventuraLoginCurrentUser = field(
        default_factory=TerraAventuraLoginCurrentUser
    )
    csrf_token: str = None
    logout_token: str = None
