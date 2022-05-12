# Example Package

[![Join the chat at https://gitter.im/mh-package/community](https://badges.gitter.im/mh-package/community.svg)](https://gitter.im/mh-package/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

## To show 
* package distribution
* package testing (unit, performance, acceptance and multi interpreter)
* logging use
* loading to pypi
<br /> 

## Usage
To install, either <br />
`pip install mh`<br /> 
`pip install git+https://github.com/MarkHallett/mh@v0.0.24` <br />
<br />
To import <br />
`import mh`<br /> 
<br /> 
Example usage   
* `print mh.EG_VAR2`<br /> 
* `print mh.testFunction()`<br /> 
* `print mh.Mh().runMh()`<br /> 
<br /> 

## To run tests  
unit `python -m unittest `<br /> 
performance `cd tests/performance; python test_perf.py`<br /> 
acceptance `cd tests/acceptance; behave mh.feature`<br /> 
multi interpreter `tox`<br /> 
