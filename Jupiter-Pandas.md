
#### Import pandas 
```python
import pandas as pd
```
#### make a dictionary of list items as data frame
```python
df_members = pd.DataFrame(members)
```
#### show data of one column as series (single square bracket)
```python
df_members['NAME'] 
df_members.NAME
```
#### show data of one column as a dataframe
```python
df_members[['NAME']]
```
#### Show only few selected columns as a dataframe
```python
df_members[['NAME', 'AGE', 'MEMBER_SINCE']]
```
### Troubleshoot error in case method name should have () paranthesis at the end or not
*  if exception is "...is not callable", then the () paranthesis are added when not necessary
*  if exception is either "... bound method", or "... function object has no attribute" then we should have paranthesis but forgot

#### First 5 rows of the dataframe use head()
```python
df_members.head()
```

#### rows and column numbers in a dataframe use shape()
```python
df_members.shape
```
#### describe column names of the collection
```python
df_members.columns
```
#### rename a column 
changes just the display, the data frame does not change
```python
df_members.rename(columns= {'NAME' : 'FIRST_LAST_NAME'})
```
#### rename a column name in the data frame 
```python
df_members = df_members.rename(columns= {'NAME' : 'FIRST_LAST_NAME'})
```
#### Modify row index in a dataframe 
changes the value in actual dataframe
```python
df_members.index = [10,11,12,13,14,15]
```
#### Reset row index 
though resets, still shows the previous custom index as a row
```python
df_members.reset_index()
```
#### Reset row index by removing the custom index
removes previous custom index as a row
```python
df_members.reset_index(drop = True)
```
#### Replaces the custom index with original index
```python
df_members = df_members.reset_index(drop = True)
```

## Reading from files and processing data

#### Read from excel
to read from excel - read_excel(), to read from csv read_csv(), to read csv from zip file read_csv("ZipFile.zip")

```python
import pandas as pd
df_members = pd.read_excel("FileName.xlsx")
```

#### Write to file 
```python
df_members.to_csv("FileName.csv")

# write to csv by ignoring the index column data
df_members.to_csv('census_new.csv', index = False)

```
#### Save the dataframe as pickle file to directly load as dataframe along with all metadata
```python
df_members.to_pickle('member_new.pickle')

# read a pickle file and load to dataframe
df_member_new = pd.read_pickle('member_new.pickle')

```

### Customize column names to make them concise or pretty
First define a list of column names that you wish to have
```python
new_col_names = ['col1', 'col2', ...]
```
Assign new column names to column
```python
df_members.columns = new_col_names
```

#### Convert a column to date time
```python
df_members.member_since = pd.to_datetime(df_members.member_since)
```

### Getting the statistical part out of data and explore
#### value_count() provides count of each item from the dataframe, also provides a list of values from the row data
user (normalize = True) parameter in value_count() to show value as percentage

```python
# show value as numbers
df_members.TYPE.value_counts()

# show value as percent
df_members.TYPE.value_counts(normalize = True)

# to convert as dataframe
df_members.TYPE.value_counts(normalize = True).reset_index()
```

### Plot Graphs
```python
import matplotlib.pyplot as plt
# first convert to dataframe then plot
df_members.TYPE.value_counts(normalize = True).plot(x = 'index', y = 'TYPE', kind = "bar")

# plot from the series without converting to dataframe
df_orders.TYPE.value_counts(normalize = True).reset_index().plot(x = 'index', y = 'TYPE', kind = "bar")
```

### Find statistical data using describe()
```python
df_members.MEDIAN_AGE.describe()
```

### Use visualization such as histogram to explore statistics
```python
df_members.MEDIAN_AGE.plot(kind = 'hist', bins = 50)
```

### Useful Opearations on Series Data in the dataframe
most math operations can be performed within columns using pandas

```python
# show number in thousands
df_members.MEDIAN_INCOME / 1000

# Conditional check
df_members.AGE >= 18.head()

# combine conditional statements
((df_members.AGE >= 18) & (df_members.GENDER == 'Female')).head()

# use single & for AND and single | for OR

# other statistical options to use on columns - sum(), max(), min(), mean(), std(), median()
# The boolean variables can be aggregated simply because pandas counts True = 1 and False = 0
((df_members.AGE >= 18) & (df_members.GENDER == 'Female')).sum()

# find matches from a list of values
df_members.CITY.isin(['New York', 'San Jose']).sum()

# find missing values using isnull()
df_members.CITY.isnull().head()

# find proportion of data with null value
# Approach 1 - count the number of null items, divide by total number of rows
df_members.CITY.isnull().sum() / df_members.shape[0]

# Approach 2 - use value counts to find percentage of null as well as not null categories
df_members.CITY.isnull().value_counts(normalize = True)

# fill in null and na values with custom text using fillna('new_string')
df_members.CITY.fillna('No City Name').head()

```

### Manipulate Date type objects using dt

```python
# returns the hour field from the data series
df_members.MEMBER_SINCE.dt.hour.head()

# find what day of the week was the date
df_members.MEMBER_SINCE.dt.weekeday.head()

# find graphical trend of dates over the week
df_members.MEMBER_SINCE.dt.weekday.value_counts().plot(kind = 'bar')

# suppress the timestamp from the date using normalize()
df_members.MEMBER_SINCE.dt.normalize().head()

# compare data against a date sent in string format only in case of less than or equal to
(df_members.MEMBER_SINCE >= '2021-01-01').sum()

# compare data for equal case (the above won't work as the string would assume 00:00:00 default timestamp to match
# to compare equally first normalize using dt function to remove time part out of the date component
(df_members.MEMBER_SINCE.dt.normalize() == '2021-01-01').sum()

# using .apply(function_name) is discouraged, as it has a huge performance impact

```

### Filter dataframe based on condition
```python
# the index numbers are from the original dataframe hence only those corresponding to filtered data is shown
df_members[df_members.MEMBER_SINCE >= '2021-01-01'].head()

# to create new index add the following to it
df_members[df_members.MEMBER_SINCE >= '2021-01-01'].reset_index(drop = True).head()

Note: Filtering dataframe does not modify the original dataframe 
```

## Combine different types of data type 
### Combine strings with integer 
```python 

("Name of the new member is : " + df_members.FIRST_NAME + " and number of pets with him are: " + df_members.PET_COUNT.astype(str)).head()

```

## Complex string functions
#### useful functon is .str
```python
# str.upper() to make UPPER case sentence, also available lower etc.
df_members.FIRST_NAME.str.upper()

# str.contains('string') to find True or False in a string
df_members.FIRST_NAME.str.contains('Utkal')

# str[1:4] for trimming string 
df_members.FIRST_NAME.str[1:4]

# str.split() to convert string to a list
df_members.ADDRESS.str.split(' ').head()

# split and show specific elements
df_members.ADDRESS.str.split(' ').str[-2:].head()
```


