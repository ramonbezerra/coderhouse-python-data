from bs4 import BeautifulSoup
import requests

url = 'https://www.python.org/blogs/'

page = requests.get(url)

if page.status_code == 200:
    soup = BeautifulSoup(page.content, 'html.parser')

    news_ul = soup.find('ul', class_='list-recent-posts')

    latest_news = news_ul.find_all('h3')

    for news in latest_news:
        link = news.find('a')['href']
        print(f"Artigo: {news.text}\nLink: {link}\n")