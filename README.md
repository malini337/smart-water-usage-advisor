# 💧 Smart Water Usage Advisor

An AI-based mini project that predicts **daily household water consumption** based on usage patterns such as number of people, showers, and laundry cycles.  
This project helps users understand whether their water usage is **sustainable or excessive**.

---

## 📌 Project Overview

Water conservation is an important global issue.  
The **Smart Water Usage Advisor** uses a **machine learning regression model** to estimate daily water usage and provide simple sustainability feedback.

This project is suitable for:
- AI / ML mini projects
- Internship submissions
- Academic demonstrations

---

## 🧠 Features

- Predicts daily water consumption (in liters)
- Uses **Train-Test split** for model training
- Simple and clean **web interface**
- Provides sustainability status:
  - ✅ Within sustainable range
  - ⚠️ High water usage
- Built using Python and Streamlit

---

## 🛠️ Technologies Used

- Python 3.13
- Pandas
- NumPy
- Scikit-learn
- Streamlit

---

## 📂 Project Structure

smart-water-usage-advisor/
│
├── app.py
├── model.py
├── water_usage_data.csv
├── requirements.txt
└── README.md


---

## 📊 Dataset Description

The dataset contains:
- Number of people
- Showers per day
- Laundry cycles per day
- Daily water usage (liters)

It is used to train a **Linear Regression** model.

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt

### 2️⃣ Run the application
streamlit run app.py

### 3️⃣ Open in browser
http://localhost:8501

🧪 Sample Demo Inputs
Parameter	Example
Number of People	3
Showers per Day	4
Laundry Cycles	1

Output:
Estimated daily water usage + sustainability message

📈 Machine Learning Workflow

Load dataset

Split data into training and testing sets

Train Linear Regression model

Predict water usage

Display result in UI

🎯 Future Enhancements

Add more usage parameters

Improve dataset size

Add charts and usage history

Deploy using cloud platforms

👩‍💻 Author

Malini S
AI / ML Mini Project
GitHub: https://github.com/malini337

