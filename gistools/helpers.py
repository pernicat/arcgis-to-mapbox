"""utility functions"""
import logging
import io
import typing as t

import requests

from .exceptions import RequestError, NotJSONError

logger = logging.getLogger(__name__)


def iterable_to_stream(iterable: t.Iterable, buffer_size=io.DEFAULT_BUFFER_SIZE):
    """
    Lets you use an iterable (e.g. a generator) that yields bytestrings as a read-only
    input stream.

    The stream implements Python 3's newer I/O API (available in Python 2's io module).
    For efficiency, the stream is buffered.

    https://stackoverflow.com/questions/6657820/how-to-convert-an-iterable-to-a-stream/20260030#20260030
    """
    class IterStream(io.RawIOBase):
        """Subclass for turing an iterator into a stream"""
        def __init__(self):  # pylint: disable=super-init-not-called
            self.leftover = None
        def readable(self):
            return True
        def readinto(self, b):
            try:
                l = len(b)  # We're supposed to return at most this much  # pylint: disable=invalid-name
                chunk = self.leftover or next(iterable)
                output, self.leftover = chunk[:l], chunk[l:]
                b[:len(output)] = output
                return len(output)
            except StopIteration:
                return 0    # indicate EOF
    return io.BufferedReader(IterStream(), buffer_size=buffer_size)


def check_response(response: requests.Response) -> t.Optional[t.Mapping]:
    """check if a reponse is valid and raises an exception if it is not"""
    if not response.ok:
        message = (
            f"status_code={response.status_code}, url={response.url} body='{response.text}'"
        )
        logger.error(message)
        raise RequestError(message)

    try:
        if not response.text:
            return None
        return response.json()
    except requests.exceptions.JSONDecodeError as e:
        logger.error("error decoding response '%s'", response.text)
        raise NotJSONError from e
