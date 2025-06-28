# 🎬 IMDb Top 250 Movies Scraper (Project Attempt)

## 📌 Description

This project was an attempt to scrape the **Top 250 Movies** from [IMDb's Top Chart](https://www.imdb.com/chart/top) using **Python**, `requests`, and `BeautifulSoup`.

The goal was to extract:
- Movie rank
- Title
- Release year
- IMDb rating
- Main star cast

and store the results in a CSV file.

---

## ⚠️ Current Status: Not Functional

Due to **IMDb's website security measures and modern web architecture**, the scraper could not successfully retrieve the required data.

### ❌ Issues Faced:
- The content is **dynamically loaded via JavaScript**
- IMDb uses **bot detection** and **anti-scraping headers**
- As a result, `requests` + `BeautifulSoup` return **empty content or HTTP 403 Forbidden errors**

---

## ✅ What Was Tried

- Setting custom `User-Agent` headers
- Inspecting DOM selectors for titles, ratings, and star cast
- Testing in Jupyter Notebook and standalone Python script

Despite these efforts, IMDb **blocked direct access** to the actual movie data.

---

## 🧩 Learnings

- Not all websites are scrape-friendly — especially major platforms like IMDb.
- Sites that render content with JavaScript often require tools like:
  - **Selenium**
  - **Playwright**
  - or official APIs
- For IMDb, better alternatives include:
  - [IMDbPY](https://imdbpy.github.io/)
  - [IMDb datasets on Kaggle](https://www.kaggle.com/search?q=imdb+top+250)

---

## 📎 Final Note

> This was my **first-ever web scraping project**. Although it didn’t yield the expected output, it was a valuable learning experience in understanding real-world scraping limitations.
