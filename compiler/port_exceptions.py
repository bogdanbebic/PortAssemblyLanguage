
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

def raise_build_error(type_of_error, line_index, src_code_line):
    raise(BuildError("BuildError-" + type_of_error + "-line{}: {}".format(line_index, src_code_line)))
