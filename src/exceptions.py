class OmniBotError(Exception):
    """Base class for bot exceptions."""
    pass

class AuthenticationError(OmniBotError):
    """Raised when API credentials fail."""
    pass
