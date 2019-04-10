# mh.py
'''
eg code to start a project with.
Seen with mh.__doc__
Can also be seen with help(mh)
'''


import mhlib.eg

EG_VAR='ABCD'

def testFunction():
    ''' returns a test string.'''

    return 'OK'


class Mh (object):
    ''' Eg class.

    Longer descripton of what the class does
    '''

    def runMh(self):
        ''' Eg class function. '''

        print ('OK RUN')
        return 100


if __name__ == '__main__':
    print ('Done')
