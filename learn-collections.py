##################### List #####################

# Lists always start with square brackets and elements are separated with commas
new_number_list = [1, 2, 3, 4, 5]
new_string_list = ["Ashok", "Venkat", "Ajay"]
new_mixed_list = [1, 1.45, "Vijay", "Suresh"]

empty_list_at_init = []
empty_list_at_init.append("Ram")
empty_list_at_init.append(1.56)
empty_list_at_init.append(new_mixed_list)
print(f"empty_list_at_init is now (1)--> {empty_list_at_init}")
empty_list_at_init.remove(1.56)
print(f"empty_list_at_init is now (2)--> {empty_list_at_init}")
# empty_list_at_init.remove("Suresh")  # error
# print(f"empty_list_at_init is now (3)--> {empty_list_at_init}")

# Split a string to make list elements using split()
city_string = "New York, Los Angeles, San Francisco, San Antonio, Washington D.C."
string_elements = city_string.split(", ")
print(f"string --> {city_string} \nlist --> {string_elements}")

# Convert list to string using join()
joined_string = (", ").join(string_elements)
print(f"list --> {string_elements} \njoined string --> {joined_string}")

# print 1st city and last city
print(
    f"first city --> {string_elements[0]} \nlast city --> {string_elements[-1]}")

# Create a subset of the list
subset_string_elements = string_elements[0:2]
print(f"subset of city list --> {subset_string_elements}")


# Loop comprehension, create lists with shortcut
upper_cities = [city.upper() for city in string_elements]
print(f"upper case list -->{upper_cities}")


##################### Dictionary #####################
stock_tesla = {"name": "Tesla", "ticker": "TSLA", "index": "NASDAQ"}
print(
    f"Stock name --> {stock_tesla['name']} \nTicker --> {stock_tesla['ticker']}")

print(f"Entire dictionary is --> {stock_tesla}")

# add new key values to existing dictionary
stock_tesla['open price'] = 604.00
print(f"Updated dictionary is --> {stock_tesla}")


stock_amazon = {"name": "Amazon", "ticker": "AMZN",
                "index": "NASDAQ", "open price": 3215.00}
stock_netflix = {"name": "Netflix", "ticker": "NFLX",
                 "index": "NASDAQ", "open price": 494.74}
stock_alphabet = {"name": "Alphabet", "ticker": "GOOG",
                  "index": "NASDAQ", "open price": 2451.75}
stock_apple = {"name": "Apple", "ticker": "AAPL",
               "index": "NASDAQ", "open price": 125.89}

stock_portfolio = [stock_tesla, stock_amazon, stock_netflix, stock_alphabet]
for stock in stock_portfolio:
    print(f"{stock['name']}\'s opening price today is {stock['open price']}")

# use list comprehension with if condition
high_priced_stocks = []
low_priced_stocks = []
[high_priced_stocks.append(stock) if stock['open price'] > 500 else low_priced_stocks.append(
    stock) for stock in stock_portfolio]

for stock in high_priced_stocks:
    print(f"{stock['name']} is a high price stock")

for stock in low_priced_stocks:
    print(f"{stock['name']} is a low price stock")

# without else clause the if statement appears different place
extreme_high_priced_stocks = []
[extreme_high_priced_stocks.append(
    stock) for stock in stock_portfolio if stock['open price'] > 1000]
for stock in extreme_high_priced_stocks:
    print(f"{stock['name']} is an extreme high price stock")
