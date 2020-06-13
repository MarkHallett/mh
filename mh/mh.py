# mh.py
''' eg code to start a project with.
Seen with mh.__doc__
Can also be seen with help(mh)
'''


import logging
import mhlib.eg


logger = logging.getLogger(__name__)


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
        logger.info('OK fo far')
        return 100


if __name__ == '__main__':
    logger.setLevel(logging.INFO)
    logger.info('Start')
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        # filename='lib1.log',
                        )
    Mh().runMh()

    logger.info('Done')
