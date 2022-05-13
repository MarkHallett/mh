# mh.py
'''eg code to start a project with.
'''

import logging
import mhlib.eg


logger = logging.getLogger(__name__)


EG_VAR='ABCD'

def testFunction():
    '''an example function that returns a string'''
    return 'OK'


class Mh (object):
    '''an example class '''

    def runMh(self):
        '''an example member function'''
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
