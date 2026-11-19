import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/5341.KL/"

response = requests.get(
    url,
    headers = {"User-Agent": "Mozilla/5.0"},
    timeout = 30,
)

response.raise_for_status()

soup = BeautifulSoup(response.text,
"html.parser")

print(soup.title.get_text())

description = soup.find ("meta", attrs={"name": "description"})

if description:
    print(description.get("content"))
else:
    print("Description not found.")

links = soup.find_all("a")

print("Starting link extraction...")
print("Total links found:", len(links))

for link in links:
    href = link.get("href")
    text = link.get_text(strip=True)

    if href and "/quote/5341.KL" in href:
        print(text, ":", href)