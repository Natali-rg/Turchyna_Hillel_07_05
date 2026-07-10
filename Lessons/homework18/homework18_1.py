import requests

BASE_URL = "https://images-api.nasa.gov"


# 1. Пошук зображень

search_url = f"{BASE_URL}/search"

search_params = {
    "q": "Curiosity rover Mars",
    "media_type": "image",
    "page_size": 20
}

response = requests.get(search_url, params=search_params)

if response.status_code != 200:
    print("Помилка при пошуку зображень")
    exit()

data = response.json()

# Отримуємо nasa_id
items = data["collection"]["items"]

nasa_ids = []

for item in items:
    nasa_id = item["data"][0]["nasa_id"]
    nasa_ids.append(nasa_id)

print("Знайдено NASA ID:")
for nasa_id in nasa_ids:
    print(nasa_id)


# 2. Отримання jpg-посилань

image_links = []

for nasa_id in nasa_ids:

    asset_url = f"{BASE_URL}/asset/{nasa_id}"

    asset_response = requests.get(asset_url)

    if asset_response.status_code != 200:
        continue

    asset_data = asset_response.json()

    files = asset_data["collection"]["items"]

    for file in files:
        href = file["href"]

        if href.lower().endswith(".jpg"):
            image_links.append(href)
            break

    if len(image_links) == 2:
        break


# 3. Завантаження зображень

file_names = [
    "mars_photo1.jpg",
    "mars_photo2.jpg"
]

for url, filename in zip(image_links, file_names):

    image = requests.get(url)

    with open(filename, "wb") as file:
        file.write(image.content)

    print(f"{filename} успішно збережено.")

print("Готово!")