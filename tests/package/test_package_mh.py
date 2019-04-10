# test1.py


import os
import sys

testdir = os.getcwd()
srcdir = '../..'
src_path =  os.path.abspath(os.path.join(testdir, srcdir))
sys.path.insert(0, os.path.abspath(src_path))


import mh
from mhlib import eg
# import mhlib.eg as eg
from  mhlib.l2 import l2



def test():
    print ('-'*20)
    print ('mh', mh.__version__)
    print ('-'*10)
    print ('file',mh)
    print ('doc',mh.__doc__)
    print ('dir',dir(mh))
    print ('.'*10)
    print ('mh api')
    print (mh.EG_VAR2)
    print (mh.testFunction() )
    mh.Mh().runMh()

    print ('.'*10)
    print ('eg api')
    print (eg)
    print (eg.EG_VAR)

    print ('.'*10)
    print ('eg l2')
    print (l2)
    dir (l2)
    print (l2.L2EG_VAR)


if __name__ == '__main__':
    test()
    print ('Done')
