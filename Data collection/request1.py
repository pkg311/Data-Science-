import requests

# Define the URL of the webpage you want to fetch
url = 'https://www.deetsdigital.com/'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200 means success)
if response.status_code == 200:
    # Print the content of the webpage
    print(response.text)
else:
    print('Failed to fetch data. Status code:', response.status_code)
    
    ##API Base Fetch
    
# Define the API endpoint URL
username = 'pkg311'

# Define the API endpoint URL
api_url = f'https://api.github.com/users/{username}'

# Send a GET request to the GitHub API
response = requests.get(api_url)

# Check if the request was successful (status code 200 means success)
if response.status_code == 200:
    # Parse the JSON response
    user_data = response.json()

    # Extract the 'public_repos' attribute from the user's data
    public_repos = user_data['public_repos']

    # Print the number of public repositories
    print(f'{username} has {public_repos} public repositories.')
else:
    print(f'Failed to fetch data. Status code: {response.status_code}')

username = 'pkg311'

# Define the API endpoint URL
api_url = f'https://api.github.com/users/{username}/repos'

# Send a GET request to the GitHub API to fetch the user's repositories
response = requests.get(api_url)

# Check if the request was successful (status code 200 means success)
if response.status_code == 200:
    # Parse the JSON response to get the list of repositories
    repos = response.json()

    # Iterate through the list of repositories and print their names
    print(f'Repositories of {username}:')
    for repo in repos:
        print(repo['name'])
else:
    print(f'Failed to fetch data. Status code: {response.status_code}')
