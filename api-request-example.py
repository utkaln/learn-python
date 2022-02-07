import requests
response = requests.get('https://api.github.com/users/utkaln/repos')
if response.status_code == 200:
    print("Request Successful")
repo_list = response.json()
for elems in repo_list:
    print(
        f'{elems["name"]} | {elems["created_at"]}')
