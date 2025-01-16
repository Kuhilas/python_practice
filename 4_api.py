import requests

# Get a request from simple api. Get it 5 more times and loop and print.

response = requests.get('https://catfact.ninja/fact')
response_json = response.json()

print(response_json)
print()

# looping 5 times

facts = []

for _ in range(5):
    response = requests.get('https://catfact.ninja/fact') 
    response_json = response.json()  
    facts.append(response_json['fact']) 

for fact in facts:
    print(fact)