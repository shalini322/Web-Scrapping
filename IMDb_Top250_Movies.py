from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

url = 'https://www.imdb.com/chart/top'
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Extract elements
movies = soup.select('td.titleColumn')
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.text.strip() for b in soup.select('td.imdbRating strong')]

movie_list = []

for index in range(len(movies)):
    movie_string = movies[index].get_text()
    movie = ' '.join(movie_string.split()).replace('.', ' ')
    movie_name = movie[len(str(index + 1)) + 1 : -7]
    year = re.findall(r'\((\d{4})\)', movie_string)[-1]
    rank = re.match(r'^(\d+)\.', movie_string).group(1)

    data = {
        "Rank": rank,
        "Movie Name": movie_name,
        "Year": year,
        "Rating": ratings[index],
        "Starring": crew[index]
    }

    movie_list.append(data)

for movie in movie_list[:10]:  # top 10 preview
    print(f"{movie['Rank']} - {movie['Movie Name']} ({movie['Year']}) - Starring: {movie['Starring']} - Rating: {movie['Rating']}")

df = pd.DataFrame(movie_list)
df.to_csv('imdb_top_250_movies.csv', index=False)
