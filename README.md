# Example Package

## To show 
* package distribution
* package testing (unit, performance, acceptance and multi interpreter)
* logging use
* loading to pypi
<br /> 

## Usage
To install, `pip install mh`<br /> 
To import `import mh`<br /> 
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
