# Learn variables, print, input
first_name_str = first_name
last_name_str = last_name
shoe_size = 8
height = "5'7\""
age = 500

print(
    f"The details I received : Your First Name : {first_name_str}, Your Last Name: {last_name_str}, Your shoe size: {shoe_size}, Your height: {height}, Your age: {age}")

# using f in print in python 3 allows to embed variable within the string
# using ''' to print a statement allows to write multi line without having to write \n

# accept user input
city_name = input("What city do you live in ? ")
print(f"The city name you provided is : {city_name}")

# show a simple future calculations
present_value = float(
    input("Please enter the present value of your investment: "))
rate_of_return = float(
    input("Please enter the interest rate on your investment: "))
number_of_periods = int(
    input("Please enter the number of months for the investment: "))
future_value = present_value * \
    ((1 + rate_of_return / 1200) ** number_of_periods)
print(f"Your future value of your investment is : ${future_value:.2f}")
