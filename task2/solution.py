import csv
from collections import defaultdict

import requests
from bs4 import BeautifulSoup


def get_animal_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    category_groups = soup.find_all(class_='mw-category-group')

    animal_count = defaultdict(int)

    for group in category_groups:
        for i in group.find_all('li'):
            animal_name = i.get_text(strip=True)
            first_letter = animal_name[0].upper()

            if 'А' <= first_letter <= 'Я':
                animal_count[first_letter] += 1

    return animal_count


def search():
    base_url = "https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту"

    current_url = base_url

    overall_count = defaultdict(int)

    while current_url:
        animal_count = get_animal_count(current_url)

        for letter, count in animal_count.items():
            overall_count[letter] += count

        response = requests.get(current_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        next_link = soup.find('a', text='Следующая страница')

        current_url = next_link['href'] if next_link else None

        if current_url and not current_url.startswith('http'):
            current_url = f"https://ru.wikipedia.org{current_url}"

    total_count = sum(overall_count.values())

    with open('beasts.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for letter, count in sorted(overall_count.items()):
            writer.writerow([letter, count])
        writer.writerow(['Всего', total_count])

    print("Обработка завершена")


if __name__ == "__main__":
    search()
