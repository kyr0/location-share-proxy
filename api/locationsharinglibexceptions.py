class InvalidCookies(Exception):
    """The cookies provided do not provide a valid session."""

class InvalidCookieFile(Exception):
    """The cookies file provided could not be parsed for cookies."""

class InvalidData(Exception):
    """The data received do not fit the expected format."""
