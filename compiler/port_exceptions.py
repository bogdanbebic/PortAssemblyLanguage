
"""
Implements Exception classes used
in the port assembly language compiler
"""

class PortException(Exception):
    """Base exception to be used in deriving exceptions
    for any port assembly language compiler error"""

    def __init__(self, msg):
        super(PortException, self).__init__(msg)
        pass

class BuildError(PortException):
    """Implements an exception used when a build error occurs"""

    def __init__(self, msg):
        super(BuildError, self).__init__(msg)
