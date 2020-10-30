"""Protocol engine errors module."""


class ProtocolEngineError(RuntimeError):
    """Base Protocol Engine error class."""
    pass


class UnexpectedProtocolError(ProtocolEngineError):
    """
    An error raised when an unexpected error occurs.

    This error is indicitive of a software bug. If it happens, it means an
    exception was raised somewhere in the stack and it was not properly caught
    and wrapped.
    """

    def __init__(self, original_error: Exception):
        super().__init__(str(original_error))
        self.original_error: Exception = original_error


class FailedToLoadPipetteError(ProtocolEngineError):
    """
    An error raised when executing a LoadPipetteRequest fails.

    This failure may be caused by:
    - An incorrect pipette already attached to the mount
    - A missing pipette on the requested mount
    """
    # TODO(mc, 2020-10-18): differentiate between pipette missing vs incorrect
    pass


class LabwareDoesNotExistError(ProtocolEngineError):
    """An error raised when referencing a labware that does not exist."""
    pass


class WellDoesNotExistError(ProtocolEngineError):
    """An error raised when referencing a well that does not exist."""
    pass


class PipetteDoesNotExistError(ProtocolEngineError):
    """An error raised when referencing a pipette that does not exist."""
    pass
