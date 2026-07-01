import numpy as np
import pandas as pd
import io

#------------------------- Data considered as missing -------------------------
#Pandas use different sentinel value depending on the type of data missing

#numpy.nan -> for numpy datatypes. Disadv of using numpy is original datatype will be coerced to np.float64 or object
x = pd.Series([1,2], dtype = np.int64).reindex([0,1,2])
print(x)
# 0    1.0
# 1    2.0
# 2    NaN
# dtype: float64

#numpy.nat for -> np.dateime64, np.timedelta64 and PeriodDType
y = pd.Series([1,2], dtype = np.dtype('timedelta64[ns]')).reindex([0,1,2])
print(y)
# 0   0 days 00:00:00.000000001
# 1   0 days 00:00:00.000000002
# 2                         NaT
# dtype: timedelta64[ns]

#NA for -> StringDType, Int64Dtype, Float64Dtype, BooleanDType and ArrowDtype
z = pd.Series([1,2], dtype = 'Int64').reindex([0,2,3])
print(z)
# 0       1
# 2    <NA> This happened because reindex matches the index label. For 0 it got an index 0 in old, but for 2 it did not get index 2 in old
# 3    <NA>
# dtype: Int64

#boolean: Standard NumPy foundations allocate a full byte (8 bits) of memory for every single True or False value.
#boolean[pyarrow]: Apache Arrow compresses the column using bitmasking. It tracks 8 boolean values inside a single byte.
a = pd.Series([True, False], dtype = 'boolean[pyarrow]').reindex([0,1,2]) 
print(a)
#0     True
# 1    False
# 2     <NA>
# dtype: bool[pyarrow]

#Detecting missing values
#use isna() or notna() -> They also consider None as missing value

ser = pd.Series([pd.Timestamp('2026-01-02'), pd.NaT])
print(ser)
# 0   2026-01-02
# 1          NaT
# dtype: datetime64[us]
print(ser.isna())
# 0    False
# 1     True
# dtype: bool
print(ser.notna())
# 0     True
# 1    False
# dtype: bool

## Standard equality operator cannot be usedto check for missing values
# None == None ->True as none is a unique defined obj representing the absence of value
# np.nan == np.nan -> False as nan is unknown and we cannot assume 2 unkown to be same
# np.NaT == np.NaT -> False
#pd.NA == pd.NA -> <NA> uses kleene's 3 valued logic that is comparing unknown to unknown should be unknown

ser = pd.Series([True, None], dtype = 'boolean[pyarrow]')
print(ser)
# 0    True
# 1     <NA> as boolean pyarrow so None converted to <NA>
# dtype: bool[pyarrow]

print(ser == pd.NA) #failure
# 0    <NA> -> is True equal to something unknown -> not known hence <NA>
# 1    <NA>
# dtype: bool[pyarrow]

print(pd.isna(ser)) #success
# 0    False
# 1     True
# dtype: bool

s = pd.Series([1, 2, None], dtype="Int64")
print(s[2] is pd.NA)
#True

#Propogation in arithmetic and logical operations: missing values propagate in operations involving NA
#When one of the operands is unknown, the outcome of the operation is also unknown.
#Exception: reductions (such as the mean or the minimum), where pandas defaults to skipping missing values.

print(pd.NA +1)
#<NA>

print(pd.NA*'a')
#<NA>

#special cases where value is known
print(pd.NA**0)
#1

print(1**pd.NA)
#1

print(pd.NA == 1)
#<NA>

print(pd.NA == pd.NA)
#<NA>

print(pd.NA < 2.5)
#<NA>

print(pd.isna(pd.NA))
#True

#Logical operators: Uses kleene logic
print(True | False)
#True

print(True | pd.NA)
#True

print(pd.NA | True)
#True

print(False | True)
#True

print(False | False)
#False

print(False | pd.NA)
#<NA>

print(False & pd.NA)
#False

print(True & pd.NA)
#<NA>

#NA cannot be used in a context where it is evaluated to a boolean, such as if condition: ... where condition can potentially be NA. 
# In such cases, isna() can be used to check for NA or condition being NA can be avoided, for example by filling missing values beforehand.
#bool(pd.NA) -> error
#ufuncs involving an ndarray and NA will return an object-dtype filled with NA values.

#Numpy unfunc
#Most unfunc functions works with NA nd generally return NA

print(np.log(pd.NA))
#<NA>

print(np.add(pd.NA, 1))
#<NA>

#------------------------- Conversion -------------------------
#if you have a DataFrame or Series using np.nan, DataFrame.convert_dtypes() and Series.convert_dtypes(), respectively, will convert your data to use the nullable data types supporting NA, such as Int64Dtype or ArrowDtype

data = io.StringIO("a,b\n,True\n2,")
df = pd.read_csv(data)
print(df)
#      a     b
# 0  NaN  True
# 1  2.0   NaN

print(df.dtypes)
# a    float64
# b     object
# dtype: object

df_conv = df.convert_dtypes()
print(df_conv)
#       a     b
# 0  <NA>  True
# 1     2  <NA>

print(df_conv.dtypes)
# a      Int64
# b    boolean
# dtype: object


#------------------------- Inserting missing data -------------------------
#The missing value sentinel used will be chosen based on the dtype.


ser = pd.Series([1., 2., 3.])

ser.loc[0] = None
print(ser)
# 0    NaN
# 1    2.0
# 2    3.0
# dtype: float64

ser = pd.Series([pd.Timestamp("2021"), pd.Timestamp("2021")])
ser.iloc[0] = np.nan
print(ser)
# 0          NaT
# 1   2021-01-01
# dtype: datetime64[us]

ser = pd.Series([True, False], dtype="boolean[pyarrow]")
ser.iloc[0] = None
print(ser)
# 0     <NA>
# 1    False
# dtype: bool[pyarrow]

#For object types, pandas will use the value given:
s = pd.Series(["a", "b", "c"], dtype=object)
s.loc[0] = None
s.loc[1] = np.nan
print(s)
# 0    None
# 1     NaN
# 2       c
# dtype: object

#-------------------------- Calculations with missing data --------------------------------------

ser1 = pd.Series([np.nan, np.nan, 2, 3])
ser2 = pd.Series([np.nan, 1, np.nan, 4])
print(ser1)
# 0    NaN
# 1    NaN
# 2    2.0
# 3    3.0
# dtype: float64

print(ser2)
# 0    NaN
# 1    1.0
# 2    NaN
# 3    4.0
# dtype: float64

print(ser1 + ser2)
# 0    NaN
# 1    NaN
# 2    NaN
# 3    7.0
# dtype: float64


#When summing data, NA values or empty data will be treated as zero.
print(pd.Series([np.nan]).sum())
#0.0

print(pd.Series([], dtype="float64").sum())
#0.0

#When taking the product, NA values or empty data will be treated as 1.
print(pd.Series([np.nan]).prod())
#1.0

print(pd.Series([], dtype ='float64').prod())
#1.0

#Cumulative methods like cumsum() and cumprod() ignore NA values by default, but preserve them in the resulting array.
ser = pd.Series([1, np.nan, 3, np.nan])
print(ser)
# 0    1.0
# 1    NaN
# 2    3.0
# 3    NaN
# dtype: float64

print(ser.cumsum())
# 0    1.0
# 1    NaN
# 2    4.0
# 3    NaN
# dtype: float64

#To override this behaviour and include NA values in the calculation, use skipna=False.
print(ser.cumsum(skipna = False))
# 0    1.0
# 1    NaN
# 2    NaN
# 3    NaN
# dtype: float64

#-------------------------- Dropping missing values --------------------------------------

#dropna() drops rows or columns with missing data.
df = pd.DataFrame([[np.nan, 1, 2], [1, 2, np.nan], [1, 2, 3]])
#print(df)
#      0  1    2
# 0  NaN  1  2.0
# 1  1.0  2  NaN
# 2  1.0  2  3.0

print(df.dropna())
#      0  1    2
# 2  1.0  2  3.0

print(df.dropna(axis =1))
#    1
# 0  1
# 1  2
# 2  2

ser = pd.Series([1, pd.NA], dtype="int64[pyarrow]")
print(ser)
# 0       1
# 1    <NA>
# dtype: int64[pyarrow]

print(ser.dropna())
# 0    1
# dtype: int64[pyarrow]
#In traditional NumPy arrays (dtype='int64'), integers cannot hold missing values. If you try to insert a missing value (None or np.nan), the entire column is forced to convert to floats (float64), which can cause precision loss.int64[pyarrow] solves this. It handles missing values using a native <NA> sentinel while keeping every other value strictly as a 64-bit integer.

#-------------------------- Filling missing data --------------------------------------

#Filling by value

#fillna() replaces NA with non-NA value
data = {"np": [1.0, np.nan, np.nan, 2], "arrow": pd.array([1.0, pd.NA, pd.NA, 2], dtype="float64[pyarrow]")}
df = pd.DataFrame(data)
print(df)
#     np  arrow
# 0  1.0    1.0
# 1  NaN   <NA>
# 2  NaN   <NA>
# 3  2.0    2.0

print(df.fillna(0))
#     np  arrow
# 0  1.0    1.0
# 1  0.0    0.0
# 2  0.0    0.0
# 3  2.0    2.0

#When the data has object dtype, you can control what type of NA values are present.
df = pd.DataFrame({"a": [pd.NA, np.nan, None]}, dtype=object)
print(df)
#       a
# 0  <NA>
# 1   NaN
# 2  None

print(df.fillna(None))
#       a
# 0  None
# 1  None
# 2  None

print(df.fillna(np.nan))
#      a
# 0  NaN
# 1  NaN
# 2  NaN

print(df.fillna(pd.NA))
#       a
# 0  <NA>
# 1  <NA>
# 2  <NA>


#However when the dtype is not object, these will all be replaced with the proper NA value for the dtype.
data = {"np": [1.0, np.nan, np.nan, 2], "arrow": pd.array([1.0, pd.NA, pd.NA, 2], dtype="float64[pyarrow]")}
df = pd.DataFrame(data)
print(df)
#     np  arrow
# 0  1.0    1.0
# 1  NaN   <NA>
# 2  NaN   <NA>
# 3  2.0    2.0

print(df.fillna(None))
#     np  arrow
# 0  1.0    1.0
# 1  NaN   <NA>
# 2  NaN   <NA>
# 3  2.0    2.0

print(df.fillna(np.nan))
#     np  arrow
# 0  1.0    1.0
# 1  NaN   <NA>
# 2  NaN   <NA>
# 3  2.0    2.0

print(df.fillna(pd.NA))
#     np  arrow
# 0  1.0    1.0
# 1  NaN   <NA>
# 2  NaN   <NA>
# 3  2.0    2.0

#Fill gaps forward or backward

print(df.ffill())
#     np  arrow
# 0  1.0    1.0
# 1  1.0    1.0
# 2  1.0    1.0
# 3  2.0    2.0

print(df.bfill())
#     np  arrow
# 0  1.0    1.0
# 1  2.0    2.0
# 2  2.0    2.0
# 3  2.0    2.0

#limit the number of NA values filled
print(df.ffill(limit=1))
#     np  arrow
# 0  1.0    1.0
# 1  1.0    1.0
# 2  NaN   <NA>
# 3  2.0    2.0


#NA values can be replaced with corresponding value from a Series or DataFrame where the index and column aligns between the original object and the filled object.
import pandas as pd
import numpy as np
dff = pd.DataFrame(np.arange(30, dtype=np.float64).reshape(10, 3), columns=list("ABC"))
dff.iloc[3:5, 0] = np.nan
dff.iloc[4:6, 1] = np.nan
dff.iloc[5:8, 2] = np.nan
print(dff)
#       A     B     C
# 0   0.0   1.0   2.0
# 1   3.0   4.0   5.0
# 2   6.0   7.0   8.0
# 3   NaN  10.0  11.0
# 4   NaN   NaN  14.0
# 5  15.0   NaN   NaN
# 6  18.0  19.0   NaN
# 7  21.0  22.0   NaN
# 8  24.0  25.0  26.0
# 9  27.0  28.0  29.0

print(dff.fillna(dff.mean()))
#        A     B          C
# 0   0.00   1.0   2.000000
# 1   3.00   4.0   5.000000
# 2   6.00   7.0   8.000000
# 3  14.25  10.0  11.000000
# 4  14.25  14.5  14.000000
# 5  15.00  14.5  13.571429
# 6  18.00  19.0  13.571429
# 7  21.00  22.0  13.571429
# 8  24.00  25.0  26.000000
# 9  27.00  28.0  29.000000


#Interpolation
#DataFrame.interpolate() and Series.interpolate() fills NA values using various interpolation methods.

df = pd.DataFrame(
    {
        "A": [1, 2.1, np.nan, 4.7, 5.6, 6.8],
        "B": [0.25, np.nan, np.nan, 4, 12.2, 14.4],
    }
)

print(df)
#      A      B
# 0  1.0   0.25
# 1  2.1    NaN
# 2  NaN    NaN
# 3  4.7   4.00
# 4  5.6  12.20
# 5  6.8  14.40

print(df.interpolate())
#      A      B
# 0  1.0   0.25
# 1  2.1   1.50
# 2  3.4   2.75
# 3  4.7   4.00
# 4  5.6  12.20
# 5  6.8  14.40

idx = pd.date_range("2020-01-01", periods=10, freq="D")

data = np.random.default_rng(2).integers(0, 10, 10).astype(np.float64)
#Computers cannot generate truly random numbers on their own. Instead, they use algorithms called Pseudo-Random Number Generators (PRNG). These algorithms take a starting number (the seed) and apply complex mathematical operations to produce a long sequence of numbers that look completely random.
ts = pd.Series(data, index=idx)

ts.iloc[[1, 2, 5, 6, 9]] = np.nan

print(ts)
# 2020-01-01    8.0
# 2020-01-02    NaN
# 2020-01-03    NaN
# 2020-01-04    2.0
# 2020-01-05    4.0
# 2020-01-06    NaN
# 2020-01-07    NaN
# 2020-01-08    0.0
# 2020-01-09    3.0
# 2020-01-10    NaN
# Freq: D, dtype: float64

ts.plot()
ts.interpolate().plot()

#Interpolation relative to a Timestamp in the DatetimeIndex is available by setting method="time"
#Setting method="time" tells Pandas to fill in missing values by looking at the actual elapsed time between dates, rather than just treating the rows as evenly spaced steps.
ts2 = ts.iloc[[0, 1, 3, 7, 9]]
print(ts2)
# 2020-01-01    8.0
# 2020-01-02    NaN
# 2020-01-04    2.0
# 2020-01-08    0.0
# 2020-01-10    NaN
# dtype: float64

print(ts2.interpolate())
# 2020-01-01    8.0
# 2020-01-02    5.0
# 2020-01-04    2.0
# 2020-01-08    0.0
# 2020-01-10    0.0
# dtype: float64

print(ts2.interpolate(method="time")) 
# 2020-01-01    8.0
# 2020-01-02    6.0
# 2020-01-04    2.0
# 2020-01-08    0.0
# 2020-01-10    0.0
# dtype: float64


#
idx = [0.0, 1.0, 10.0]

ser = pd.Series([0.0, np.nan, 10.0], idx)

print(ser) 
# 0.0      0.0
# 1.0      NaN
# 10.0    10.0
# dtype: float64

print(ser.interpolate())
# 0.0      0.0
# 1.0      5.0
# 10.0    10.0
# dtype: float64

ser.interpolate(method="values")
# 0.0      0.0
# 1.0      1.0
# 10.0    10.0
# dtype: float64

#If you are dealing with a time series that is growing at an increasing rate, use method='barycentric'.
#If you have values approximating a cumulative distribution function, use method='pchip'.
#To fill missing values with goal of smooth plotting use method='akima'.

#When interpolating via a polynomial or spline approximation, you must also specify the degree or order of the approximation:

print(df.interpolate(method="spline", order=2))
#           A          B
# 0  1.000000   0.250000
# 1  2.100000  -0.428598
# 2  3.404545   1.206900
# 3  4.700000   4.000000
# 4  5.600000  12.200000
# 5  6.800000  14.400000

print(df.interpolate(method="polynomial", order=2))
#           A          B
# 0  1.000000   0.250000
# 1  2.100000  -2.703846
# 2  3.451351  -1.453846
# 3  4.700000   4.000000
# 4  5.600000  12.200000
# 5  6.800000  14.400000

#Comparing several methods.

np.random.seed(2)
ser = pd.Series(np.arange(1, 10.1, 0.25) ** 2 + np.random.randn(37))
missing = np.array([4, 13, 14, 15, 16, 17, 18, 20, 29])
ser.iloc[missing] = np.nan
methods = ["linear", "quadratic", "cubic"]
df = pd.DataFrame({m: ser.interpolate(method=m) for m in methods})
df.plot()