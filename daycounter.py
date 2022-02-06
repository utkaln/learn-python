from datetime import datetime
user_input = input(
    "Enter your goal and a date. Example: Learn Serverless : 12/31/22\n")

user_input_list = user_input.split(":")
goal = user_input_list[0]
deadline = user_input_list[1]
print(goal)
print(deadline)

target_date = datetime.strptime(deadline, "%d/%m/%y")
current_date = datetime.today()
time_to_target = target_date - current_date
print(f"time from today --> {time_to_target.days}")
