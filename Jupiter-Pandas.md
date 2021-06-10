
#### Import pandas 
> import pandas as pd

#### make a dictionary of list items as data frame
> df_members = pd.DataFrame(members)

#### show data of one column as series (single square bracket)
> df_members['NAME'] 
> df_members.NAME

#### show data of one column as a dataframe
> df_members[['NAME']]

#### Show only few selected columns as a dataframe
>df_members[['NAME', 'AGE', 'MEMBER_SINCE']]

### Troubleshoot error in case method name should have () paranthesis at the end or not
*  if exception is "...is not callable", then the () paranthesis are added when not necessary
*  if exception is either "... bound method", or "... function object has no attribute" then we should have paranthesis but forgot

#### First 5 rows of the dataframe use head()
> df_members.head()

#### rows and column numbers in a dataframe use shape()
> df_members.shape

#### describe column names of the collection
> df_members.columns

#### rename a column 
changes just the display, the data frame does not change
> df_members.rename(columns= {'NAME' : 'FIRST_LAST_NAME'})

#### rename a column name in the data frame 
> df_members = df_members.rename(columns= {'NAME' : 'FIRST_LAST_NAME'})

#### Modify row index in a dataframe 
changes the value in actual dataframe
> df_members.index = [10,11,12,13,14,15]

#### Reset row index 
though resets, still shows the previous custom index as a row
> df_members.reset_index()

#### Reset row index by removing the custom index
removes previous custom index as a row
> df_members.reset_index(drop = True)

#### Replaces the custom index with original index
> df_members = df_members.reset_index(drop = True)


## Reading from files and processing data

#### Read from excel
> import pandas as pd
> df_members = pd.read_excel("FileName.xlsx")

