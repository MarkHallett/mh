'''
example of an internal module
'''

import time
from mhlib.l2 import l2


EG_VAR='abcd'

def test():
    '''example intenal function'''
    return 'ok'

class MhEg (object):
    '''example intenal class'''
    def runMhEg(self):
        '''example member function of an intenal class'''
        return 10

    def slow(self):
        '''no documentation'''
        t = 3
        time.sleep(t)
        return


    def call_external_func(self):
        '''no documentation'''
        x = l2.L2Mh()
        y = x.slow()
        return y



if __name__ == '__main__':
    pass

