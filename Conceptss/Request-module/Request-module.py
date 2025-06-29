
# The requests module in Python is used to send HTTP requests. It’s one of the most popular libraries for working with APIs and web pages. You can use it to make GET, POST, PUT, DELETE, and other HTTP requests easily.

# When to Use requests?
# Accessing or testing REST APIs
#
# Scraping websites (along with BeautifulSoup)
#
# Sending form data or JSON to servers
#
# Downloading images, files, etc.



# Basic Example – GET request

import requests

response = requests.get("https://api.github.com")

print(response.status_code)       # HTTP status code (e.g. 200)
print(response.text)              # Raw HTML or JSON response
print(response.json())            # Convert JSON to Python dictionary


# POST Request (send data to a server)

import requests

data = {"username": "farhan", "password": "1234"}
response = requests.post("https://httpbin.org/post", data=data)

print(response.status_code)
print(response.json())


#  Other Useful Things
# Headers (send user-agent, tokens, etc.)

headers = {
    "User-Agent": "my-app",
    "Authorization": "Bearer your_token_here"
}
response = requests.get("https://api.example.com/data", headers=headers)


# Query Parameters (for filtering/searching)

params = {"page": 1, "limit": 5}
response = requests.get("https://api.example.com/items", params=params)


# Timeouts (stop waiting forever)

response = requests.get("https://example.com", timeout=5)


# Handling Errors

if response.status_code == 200:
    print("Success")
else:
    print("Failed:", response.status_code)


# Download a File Example

url = "https://example.com/image.png"
response = requests.get(url)

with open("image.png", "wb") as file:
    file.write(response.content)








































































