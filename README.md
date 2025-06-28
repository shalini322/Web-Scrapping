📌 Description
This project was an attempt to scrape the Top 250 Movies from IMDb's Top Chart using Python, requests, and BeautifulSoup.

⚠️ Current Status: Not Functional
Due to IMDb's security policies and modern web structure:

The content is dynamically loaded with JavaScript

IMDb employs bot detection and anti-scraping headers

As a result, requests + BeautifulSoup do not return usable HTML, and the scraper fails to extract data (returns empty or 403 errors)

✅ What Was Tried
Setting custom User-Agent headers

Inspecting selectors for titles, ratings, and crew info

Testing in Jupyter Notebook and Python script

Still, the website blocked direct access to required content.

🧩 Learnings
Not all websites are scrape-friendly, especially big platforms like IMDb.

JavaScript-rendered content needs tools like Selenium, Playwright, or APIs.

Best alternative: use official APIs, IMDbPY, or datasets from Kaggle.
