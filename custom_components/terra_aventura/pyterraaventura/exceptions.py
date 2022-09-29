"""Exceptions used by PyTerraAventura."""


class PyTerraAventuraException(Exception):
    """Base class for all exceptions raised by PyTerraAventura."""


class BadCredentialsException(Exception):
    """Raised when credentials are incorrect."""


class NotAuthenticatedException(Exception):
    """Raised when session is invalid."""
