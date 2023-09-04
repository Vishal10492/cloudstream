import requests
url = "https://recloudstream.github.io/devs/scraping/"
response = requests.get(url)
print(response.text)  # Prints the readme