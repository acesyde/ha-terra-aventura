"""Models used by PyTerraAventura."""

from dataclasses import dataclass, field


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


@dataclass
class TerraAventuraUserReponseFieldStatistics:
    """TerraAventura User Field Statistics."""

    kcalsUser: int
    kcalsNextLevel: int
    kcalPercent: int
    kcalLevel: str
    kcalClass: str
    kmsUser: float
    kmsNextLevel: int
    kmsLevel: str
    kmsPercent: int
    kmsClass: str
    cachesTotales: int
    cachesPercent: int
    cachesUser: int


@dataclass
class TerraAventuraUserResponse:
    """TerraAventura User Response."""

    uid: str = None
    name: str = None
    field_statistics: TerraAventuraUserReponseFieldStatistics = field(
        default_factory=TerraAventuraUserReponseFieldStatistics
    )


@dataclass
class TerraAventuraJokerResponse:
    """TerraAventura Joker Response."""

    jokers_activated: bool = None
    jokers_max: int = None
    trials_activated: bool = None
    trials_max: int = None
    comments_before_jokers: int = None
