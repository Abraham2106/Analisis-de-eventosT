import numpy as np
import pandas as pd
import DetailedPrint 
# Imports needed 
"""
    Series: One-dimensional array capable of holding any data type.
    The axis labels are referred to as index.
    The basic method to create a Series is to call: 
"""

s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])

# The data is printed along with their respective index
# print(s)
# print()
# It prints the index and their data type
# print(s.index)
# print()
'''
    Series can be instantiated from dicts
'''
d = {"a": 4, "b": 5, "c": 3}
d = pd.Series(d)
'''
print(d)
print()
'''
# If an index is passed, the data with the label will be pulled out
# print(pd.Series(d, index=["a", "b", "d", "c"]))
# print()
# When there's an index without data, a not-a-number marker (NaN) is passed  

# If a scalar value is given, it'll be propagated to match the index length 
a = pd.Series(5.0, index=["a", "b", "c", "d", "e"])

# series.iloc[] purely integer-based index search, it can be an integer, an array of integers, or a slice object with ints
 
# print(d.iloc[:-1])
# print()

"""
    A pandas series has a single dtype.
    Also, it can be accessed as an array to do operations without the index.
    <<<<<<<<<Sort>>>>>>>>>
    Values can be sorted using Series.sort_values(ascending=bool).
    Values will be sorted in ascending order by default.
"""
# print(a.array)
# print()
# print(d.sort_values(ascending=False))

'''
    Test #1
    Let's make a dictionary with values ranging from 1 to 10 and a, b, c, d, e, f, g, h, j, k as their index.
    The dictionary is created and then converted into a pandas series.
'''
test1 = {"a":1, "b": 2, "c":3, "d": 4,"e":5,"f":6,"g":7,"h":8, "j":9,"k":10}
test1 = pd.Series(test1)


