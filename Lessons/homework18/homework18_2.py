import os
import requests

BASE_URL = "http://127.0.0.1:8080"

IMAGE_NAME = "mars_photo1.jpg"


# POST /upload


with open(IMAGE_NAME, "rb") as image:
    files = {
        "image": image
    }

    response = requests.post(
        f"{BASE_URL}/upload",
        files=files
    )

print("POST status:", response.status_code)
print(response.json())

if response.status_code != 201:
    print("Помилка завантаження!")
    exit()

image_url = response.json()["image_url"]

# Отримуємо ім'я файлу з URL
filename = os.path.basename(image_url)

print("Filename:", filename)


# GET /image/<filename>


response = requests.get(
    f"{BASE_URL}/image/{filename}",
    headers={
        "Content-Type": "text"
    }
)

print("\nGET status:", response.status_code)
print(response.json())


# DELETE /delete/<filename>


response = requests.delete(
    f"{BASE_URL}/delete/{filename}"
)

print("\nDELETE status:", response.status_code)
print(response.json())