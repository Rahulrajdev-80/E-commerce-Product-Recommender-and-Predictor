import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv(r"C:\PROJECT DOCUMENTS\SANJAY DOC\CONFERENCE AND JOURNALS\PHASE 2 PROJECT\Lokesh\CONFERENCE WORK\finals\rahul\ecommerce_product_dataset.csv")

# Encode category
le = LabelEncoder()
df["CategoryEncoded"] = le.fit_transform(df["Category"])
df["HighSales"] = (df["Sales"] > df["Sales"].median()).astype(int)

# Train model
X = df[["Price", "Rating", "NumReviews", "StockQuantity", "Discount", "CategoryEncoded"]]
y = df["HighSales"]
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Streamlit UI
st.title("🛍️ E-commerce Product Predictor and Recommender")

st.sidebar.header("Product Input")
price = st.sidebar.slider("Price", float(df.Price.min()), float(df.Price.max()), float(df.Price.mean()))
rating = st.sidebar.slider("Rating", float(df.Rating.min()), float(df.Rating.max()), float(df.Rating.mean()))
num_reviews = st.sidebar.slider("Reviews", int(df.NumReviews.min()), int(df.NumReviews.max()), int(df.NumReviews.mean()))
stock = st.sidebar.slider("Stock", int(df.StockQuantity.min()), int(df.StockQuantity.max()), int(df.StockQuantity.mean()))
discount = st.sidebar.slider("Discount", 0.0, 1.0, float(df.Discount.mean()))
category = st.sidebar.selectbox("Category", df["Category"].unique())
cat_encoded = le.transform([category])[0]

# Predict sales
input_data = pd.DataFrame([[price, rating, num_reviews, stock, discount, cat_encoded]],
                          columns=["Price", "Rating", "NumReviews", "StockQuantity", "Discount", "CategoryEncoded"])
prediction = model.predict(input_data)[0]
st.subheader("Sales Prediction:")
st.success("🔼 High Sales Expected" if prediction else "🔽 Low Sales Expected")

# Recommend products
def recommend_products(category, top_n=5):
    filtered = df[df["Category"] == category]
    return filtered.sort_values("Sales", ascending=False).head(top_n)[["ProductName", "Price", "Rating", "Sales"]]

st.subheader(f"Top Recommended Products in '{category}'")
st.dataframe(recommend_products(category).reset_index(drop=True))
