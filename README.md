# 🎓 Online Course Recommendation System

A Python-based web app that recommends courses based on user preferences using web scraping and machine learning.

## 🚀 Features

* Scrapes course data from Coursera (public pages)
* Filters by domain, sub-domain, level, duration, and price
* Content-based recommendation system
* Interactive Streamlit UI
* Clickable course links

## 🧠 Algorithms Used

* Content-Based Filtering
* TF-IDF
* Cosine Similarity
* Rule-Based Filtering

## 📁 Project Structure

course_recommender/

* scraper.py
* model.py
* app.py
* coursera_courses.csv
* requirements.txt

## ⚙️ Setup

1. Install dependencies
   pip install -r requirements.txt

2. Run scraper
   python scraper.py

3. Run app
   streamlit run app.py

## 📌 Output

Displays recommended courses with title, domain, level, duration, price, mentor, and link.

## 🔮 Future Improvements

* Hybrid recommendation system
* Better scraping using Selenium
* Add ratings and popularity
