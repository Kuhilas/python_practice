import requests

# Make a program that retrieves Python repos from the Github API

response = requests.get('https://api.github.com/search/repositories?q=language:python')
response_json = response.json()

# Iterate trough the list of repositories. Print data line by line, in the following format:Forks:{forks}. Name:{name} Description:{description}

# Get the number of items

number_of_items = len(response_json["items"])

# Loop trough the number of items in the response

for item in range(number_of_items):
    repo = response_json["items"][item]

    name = repo["name"]
    description = repo["description"]
    forks = repo["forks_count"]

    print(f"Forks: {forks}. Name: {name} Description: {description}")

