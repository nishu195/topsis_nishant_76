# TOPSIS implementation in python for multi-criteria decision making

```
This package has been created based on Project 1 of course UCS633(DATA ANALYSIS AND VISUALISATION ) Thapar University, Patiala
Nishant Goel  
COE17
Roll number: 101703376
```

Output is a list with rankings of different objects.
 - also includes **Best_performance_object** 

## Installation
`pip install topsis_nishant_76`

*Recommended - test it out in a virtual environment.* 

## Upgrade
`pip install topsis_nishant_76 --upgrade`

## To use via command line
`topsis_cli mydata.csv '1,2,1,1' '-,+,+,+'`

First argument is filename with .csv extension. The .csv file is assumed to have a structure similar to one provided in topsis_nishant_76/mydata.csv

That is, the .csv file should have a header with column names and first column should only list alternatives and not attribute values.

## To use in .py script
```
from topsis_nishant_76 import topsis_nish
"""
decision_matrix is 2D numpy array, weights is a string seperated with ',' and impacts is a string of the form '+,-,+,-' 
where + indicates benefit and - indicates cost
"""
topsis_nish('mydata.csv','1,2,1,1','+,-,+,+')
```