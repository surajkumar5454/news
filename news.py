import requests
import json

# Your API key
api_key = '20157af1d27548e38a2925331bf1c2d3'

# The topic you want to search for
topic = 'India to deploy ballistic missiles near China and Pakistan'

# Make the request
response = requests.get('https://newsapi.org/v2/everything?q=' + topic + '&apiKey=' + api_key)

# Get the JSON data from the response
data = json.loads(response.text)
print(data)
# Print the total number of articles found
print('Total articles found:', data['totalResults'])

# Print the title, description, and url for each article
for article in data['articles']:
    print('Title:', article['title'])
    print('Description:', article['description'])
    print('Url:', article['url'])
    print('Image:', article['urlToImage'])
    print('Publish Date:', article['publishedAt'])
    print()

