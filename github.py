import requests

github_username = input("Please provide a GitHub username to retrieve public repositories\n")

response = requests.get(f"https://api.github.com/users/{github_username}/repos")
project_list = response.json()

for item in project_list:
    print(f'Name: {item["name"]} \nURL: {item["html_url"]}\n')