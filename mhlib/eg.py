# eg.py
'''
eg lib code
Example imports of EG_VAR,
import mhlib, print (mhlib.eg.EG_VAR)
import mhlib.eg as eg, print (eg.EG_VAR)
from mhlib import eg, print (eg.EG_VAR)
from mhlib.eg import EG_VAR as eg_var, print (eg_var)
'''

import time
from mhlib.l2 import l2


EG_VAR='abcd'

def test():
    ''' returns a test string '''
    return 'ok'

class MhEg (object):
    ''' eg class doc string '''
    def runMhEg(self):
        ''' doc string for member function '''
        return 10

    def slow(self):
         t = 3
         time.sleep(t)
         return


    def call_external_func(self):
        x = l2.L2Mh()
        y = x.slow()
        return y



if __name__ == '__main__':
    pass
