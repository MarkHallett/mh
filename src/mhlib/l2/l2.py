'''Documentation for l2.py...'''

import time

L2EG_VAR='efgh'


def L2Test() -> str:
    '''L2 test funtion'''
    return 'ok2'


class L2Mh (object):
    """class L2Mh documentation"""

    def run(self) -> int:
        """Simple function"""
        return 10

    def slow(self) -> int:
        """Example slow function."""
        t = 5
        time.sleep(t)
        return t
