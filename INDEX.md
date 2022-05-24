# Documentation of the Python package mh

## Purpose

The mh package is a small package that can be used as a template for larger packages

## Install `mh`
To download the package from pypi, and install into the python site-packages

    pip install mh

To install from github from a version tag eg `v0.0.32`
    
    pip install git+https://github.com/MarkHallett/mh@v0.0.32


!!! warning
    Use a virtual env before installing

## Use
From the exposed interface provided you can run

```python
import mh
print(mh.__version__)    # the version of the package
print(mh.EG_VAR2)        # a variable from the package
print(mh.testFunction()) # a function from the package
print(mh.Mh().runMh())   # run a function of an Mh object
```

For more information use

* `dir(mh)`
* `help(mh)`
* the [Code Reference](reference/mh/mh) tab, which also shows the details of the internal implementation

