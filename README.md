# 🛍️ E-commerce Product Sales Predictor and Recommender

This Streamlit app predicts whether a product is likely to achieve **high sales** based on key features like price, rating, stock, reviews, and discount. It also recommends top-selling products in the same category using data from Flipkart's fashion product dataset.

---

## 📌 Features

- Predicts **High Sales** or **Low Sales** using a Logistic Regression model
- Recommends top products based on sales for the selected category
- Interactive UI built with Streamlit
- Uses a real Excel dataset: `output.xlsx`

---

## 📂 Dataset

The dataset is an Excel file containing product data from Flipkart, with the following required columns:

- `ProductName`
- `Price`
- `Rating`
- `NumReviews`
- `StockQuantity`
- `Discount`
- `Category`
- `Sales`

Ensure these columns exist in your Excel file.

---

## 🚀 How to Run

### 🔹 Option 1: Local (with Python + Streamlit)

1. Clone the repository or download the code.

2. Place your Excel dataset (`output.xlsx`) inside the project folder.

3. Install required packages:
   ```bash
   pip install pandas scikit-learn streamlit openpyxl
Run the app:

streamlit run app.py

Model

Algorithm: Logistic Regression

Target Variable: HighSales (1 if sales > median, else 0)

Features: Price, Rating, NumReviews, StockQuantity, Discount, Encoded Category

Output

Sales Prediction: Indicates whether the given product is likely to perform well

Top Recommendations: Lists top 5 products with highest sales in the same category

Screenshots
![Screenshot (261)](https://github.com/user-attachments/assets/e2871493-f570-4bfd-a4f7-433d27b2c907)
