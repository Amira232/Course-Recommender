import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class CourseRecommender:

    def __init__(self, file_path):
        self.df = pd.read_csv("coursera_courses.csv")

        # Normalize column names (VERY IMPORTANT)
        self.df.columns = self.df.columns.str.strip().str.lower().str.replace(" ", "_")

        # Check required columns
        required_columns = [
            "course_title", "domain", "sub_domain",
            "level", "duration", "price", "mentor", "url"
        ]

        for col in required_columns:
            if col not in self.df.columns:
                raise ValueError(f"Missing column: {col}")

        # Fill missing values
        self.df.fillna("", inplace=True)

        # Convert numeric columns safely
        self.df["duration"] = pd.to_numeric(self.df["duration"], errors="coerce").fillna(0)
        self.df["price"] = pd.to_numeric(self.df["price"], errors="coerce").fillna(0)

        # Combine features for similarity
        self.df["combined_features"] = (
            self.df["domain"] + " " +
            self.df["sub_domain"] + " " +
            self.df["level"] + " " +
            self.df["mentor"]
        )

        # TF-IDF vectorizer
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.feature_matrix = self.vectorizer.fit_transform(self.df["combined_features"])


    def recommend_courses(self, domain, sub_domain, level, duration, price_range, top_n):

        df_filtered = self.df.copy()

        # FILTERING 

        if domain != "All":
            df_filtered = df_filtered[df_filtered["domain"] == domain]

        if sub_domain:
            df_filtered = df_filtered[
                df_filtered["sub_domain"].str.contains(sub_domain, case=False, na=False)
            ]

        if level != "All":
            df_filtered = df_filtered[df_filtered["level"] == level]

        # Duration filter
        df_filtered = df_filtered[df_filtered["duration"] <= duration]

        # Price filter
        min_price, max_price = price_range
        df_filtered = df_filtered[
            (df_filtered["price"] >= min_price) &
            (df_filtered["price"] <= max_price)
        ]

        # If no results
        if df_filtered.empty:
            return pd.DataFrame()

        # SIMILARITY

        input_text = f"{domain} {sub_domain} {level}"
        input_vector = self.vectorizer.transform([input_text])

        similarity_scores = cosine_similarity(input_vector, self.feature_matrix).flatten()

        # Add scores correctly
        df_filtered = df_filtered.copy()
        df_filtered["score"] = similarity_scores[df_filtered.index]

        # Sort
        recommendations = df_filtered.sort_values(by="score", ascending=False)

        return recommendations.head(top_n)