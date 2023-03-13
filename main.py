import requests
from bs4 import BeautifulSoup

#Запит
def books(query):
    url = "https://www.googleapis.com/books/v1/volumes"
    parametr = {
        "q": query
    }
    response = requests.get(url, params=parametr)
    data = response.json()
    return data

# Пошук
def find_books():
    query = input("Введіть запит для пошуку книг: ")
    data = books(query)
    for i in data["items"]:
        volume_info = i["volumeInfo"]
        print(f"Назва: {volume_info['title']}")
        if "authors" in volume_info:
            print(f"Автори: {', '.join(volume_info['authors'])}")
        if "description" in volume_info:
            print(f"Опис: {volume_info['description']}")
        print("\n")

if __name__ == "__main__":
    find_books()