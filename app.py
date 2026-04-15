import streamlit as st
from model import CourseRecommender

# Load recommender
recommender = CourseRecommender("data/coursera_courses.csv")
df = recommender.df

# Page config
st.set_page_config(page_title="Course Recommender", layout="wide")

# Title
st.title("🎓 Online Course Recommendation System")
st.markdown("### Find the best courses based on your preferences")

# Sidebar
st.sidebar.header("Filter Options")

# Domain dropdown
domains = ["All"] + sorted(df["domain"].unique().tolist())
domain = st.sidebar.selectbox("Domain", domains)

# Sub-domain text
sub_domain = st.sidebar.text_input("Sub Domain")

# Level dropdown
levels = ["All"] + sorted(df["level"].unique().tolist())
level = st.sidebar.selectbox("Level", levels)

# Duration slider
duration = st.sidebar.slider("Max Duration (months)", 1, 24, 6)

# Price slider
min_price = int(df["price"].min())
max_price = int(df["price"].max())

price_range = st.sidebar.slider(
    "Price Range",
    min_value=min_price,
    max_value=max_price,
    value=(min_price, max_price)
)

# Top N
top_n = st.sidebar.slider("Number of Recommendations", 1, 10, 5)

# Button
if st.sidebar.button(" Recommend Courses"):

    results = recommender.recommend_courses(
        domain, sub_domain, level, duration, price_range, top_n
    )

    if results.empty:
        st.warning("❌ No courses found. Try different filters.")
    else:
        st.success(f"✅ Showing Top {len(results)} Courses")

        for _, row in results.iterrows():
            with st.container():
                st.markdown(f"##  {row['course_title']}")

                col1, col2, col3 = st.columns(3)

                col1.write(f"**Domain:** {row['domain']}")
                col1.write(f"**Sub Domain:** {row['sub_domain']}")

                col2.write(f"**Level:** {row['level']}")
                col2.write(f"**Duration:** {row['duration']} months")

                col3.write(f"**Price:** ₹{row['price']}")
                col3.write(f"**Mentor:** {row['mentor']}")

                st.markdown(f"[🔗 Go to Course]({row['url']})")

                st.markdown("---")