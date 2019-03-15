# eg.py
'''
eg code
'''


import mhlib.eg

EG_VAR='ABCD'

def testFunction():
    ''' returns a test string '''
    return 'OK'

class Mh (object):
    ''' Eg class '''

    def runMh(self):
        ''' Eg class function '''
        print ('OK RUN')
        return 100


if __name__ == '__main__':
    print ('ok')
    print (EG_VAR)
    print (dir(mhlib.eg))
    print (mhlib.eg.EG_VAR)
    print ('Done')
