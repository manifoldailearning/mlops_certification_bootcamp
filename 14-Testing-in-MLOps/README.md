# Assertions 
```
assert x==y              | Basic Equality Check
assert x in y            | Membership Testing
assert isinstance(x,t)   | Type Check
assert x>y               | Numeric comparision
assert not x             | Boolean negation
```

# Pytest-coverage
```
pip install pytest-cov pytest-html

pytest --cov=/. --cov-report=term --cov-report=html --html=reports/report.html --self-contained-html


--cov : folder where the code coverage report to be generated for
--html=reports/report.html : generate the html report on reports folder
--cov-report=term : print the coverage summary on terminal
--self-contained-html : embds the CSS/JS on the html so that we can view it offline
```