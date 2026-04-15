🎓 Online Course Recommendation System

A fully functional Online Course Recommendation System built using Python, Machine Learning, Web Scraping, and Streamlit.
This system recommends courses based on user preferences such as domain, sub-domain, level, duration, and price.

🚀 Features
🔍 Scrapes real course data from Coursera (public pages)
📊 Supports multiple domains and sub-domains
🎯 Smart filtering based on user inputs
🤖 Content-based recommendation system
⚡ Fast and interactive Streamlit UI
🎨 Clean and professional interface with card-style results
🔗 Direct links to course pages
🧠 Recommendation System

Algorithms Used:
Content-Based Filtering
TF-IDF Vectorization
Cosine Similarity (optional enhancement)
Rule-Based Filtering

Workflow:
User Input → Filtering → Ranking → Top-N Recommendations

🗂️ Project Structure
course_recommender/
│
├── scraper.py               # Web scraping script
├── model.py                 # Recommendation logic
├── app.py                   # Streamlit frontend
├── coursera_courses.csv     # Dataset
├── requirements.txt         # Dependencies

 Data Collection
Data is scraped from publicly available course listing pages of Coursera
Ethical scraping practices followed (no login / restricted content)

Dataset Columns:
course_title
domain
sub_domain
level
duration
is_paid
price
mentor
url

🎯 User Inputs (Frontend)
📂 Domain (Dropdown)
🔎 Sub Domain (Text Input)
📊 Level (Dropdown)
⏳ Duration (Slider)
💰 Price Range (Slider)
📌 Number of Recommendations (Slider)

🖥️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/course-recommender.git
cd course-recommender
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Run scraper (to generate dataset)
python scraper.py
4️⃣ Run the application
streamlit run app.py

Output
Displays recommended courses with:
Course Title
Domain & Sub-domain
Level
Duration
Price
Mentor
Clickable Course Link

⚠️ Limitations
Uses static scraping (limited data from dynamic pages)
Some fields like price/duration may be approximated
No user login or personalization

🔥 Future Enhancements
✅ Hybrid Recommendation System (Content + Popularity)
✅ Use Selenium for advanced scraping
✅ Add course ratings & reviews
✅ Personalized recommendations (user history)
✅ Deploy on Streamlit Cloud

Use Cases
Students exploring online courses
Beginners choosing learning paths
Career switchers finding relevant courses

📌 Conclusion

This project demonstrates how Machine Learning + Web Scraping + UI design can be combined to build a real-world recommendation system.
