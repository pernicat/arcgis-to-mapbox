"""exception classes"""


class RequestError(Exception):
    """Request Failure exception"""


class NotJSONError(Exception):
    """The result is not json"""
