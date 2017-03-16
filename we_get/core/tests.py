"""
Copyright (c) 2016-2017 we-get developers (https://github.com/0xl3vi/we-get/)
See the file 'LICENSE' for copying.
"""

import sys
from we_get.core.utils import msg_error

class Tests(object):
    """ run tests for Python version, platforms changes.
    """
    def __init__(self):
        self.test = 0;

    def python(self):
        """Python version test.
           we are not using Python 2 due the end of support in 2020.
        """
        if sys.version_info.major != 3:
            msg_error("please use Python 3 to run we-get.", True)

    def init(self):
        self.python()
