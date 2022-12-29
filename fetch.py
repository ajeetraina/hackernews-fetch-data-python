import requests

# Set the search term and API endpoint
search_term = "docker"
api_endpoint = f"https://hn.algolia.com/api/v1/search?query={search_term}"

# Send the request to the API endpoint
response = requests.get(api_endpoint)

# Check the status code of the response
if response.status_code == 200:
    # If the request is successful, get the data from the response
    data = response.json()
    # Extract the relevant data from the response
    results = data["hits"]
    # Print the results in a tabular format
    print("Title | URL | Points | Author | Date")
    for result in results:
        print(f"{result['title']} | {result['url']} | {result['points']} | {result['author']} | {result['created_at']}")
else:
    # If the request is not successful, print an error message
    print("An error occurred while fetching the data from Hacker News")
