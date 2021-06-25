### Examples are used from alpha advantage
> Useful Resource https://pypi.org/project/alpha-vantage/ 

```python
import pandas as pd
# install alpha_vantage python package, use ! to install directly in jupyter
!pip install alpha_vantage

# import timeseries
from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='********')

# instead of above approach, secure the API key in a separate file
with open('alpha-vantage-api-key-utkal.txt') as file:
    alphavantage_api_key = file.read()
ts = TimeSeries(key= alphavantage_api_key)

# read data from time series, in primitive way (not as pandas dataframe)
data, meta_data = ts.get_daily('AMZN')

# then manually load to pandas dataframe
pd.DataFrame(data).transpose()

# instead of above steps use directly provided python method to convert to dataframe directly
ts = TimeSeries(key= alphavantage_api_key, output_format = 'pandas')

# to change from default number of rows returned which is 100, use the parameter to get full data
data, meta_Data = ts.get_daily('AMZN', outputsize='full')

```
### Web scraping
#### Use beautiful soup to scrap a website and get data in a meaningful way

```python
# first import request package to deal with web requests
import requests

# import Beautiful Soup library that ships with Anaconda (No install of BS is required0
from bs4 import BeautifulSoup

response = requests.get('https://www.google.com')
response.status_code
response.text

# Use BeautifulSoup to prettify the html scraped
soup = BeautifulSoup(response.text)
print(soup.prettify())

# find all links from the webpage find() --> finds the first occurrence, find_all() --> finds all occurrences
links = soup.find_all('a')

# print the link names
for link in links:
    print(link.text)
    
# search for tag
soup.find_all('a')

# search for class
soup.find_all(class_ = 'a')

# search for both 
soup.find_all('a', class_='class_name')

# find specific elements within a tag by applying hierarchical calls of find method
for link in links:
        print(link.get('href'))

```
