📊 Employee Job Change Prediction

A Machine Learning web application built with Streamlit that predicts whether an employee is likely to stay with the company or change jobs based on their personal, educational, and professional details.

---

🚀 Features

- 🎨 Modern and responsive Streamlit interface
- 🖼️ Hero banner with custom background image
- 📝 Employee information form with categorized inputs
- 🤖 Machine Learning-based prediction
- 📈 Prediction confidence score
- 📊 Interactive probability charts
- 💻 Easy to deploy on Streamlit Community Cloud

---

🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- Matplotlib
- Joblib
- HTML & CSS

---

📂 Project Structure

employee_retention_prediction/
│── app.py
│── employee_model.pkl
│── encoders.pkl
│── banner.jpg
│── aug_train.csv
│── aug_test.csv
│── predictions.csv
│── employee_retention_prediction.ipynb
│── requirements.txt
│── README.md

---

⚙️ Installation

Clone the repository

git clone https://github.com/shreyashende2005-afk/employee_retention_prediction.git

Move into the project directory

cd employee_retention_prediction

Install dependencies

pip install -r requirements.txt

Run the application

streamlit run app.py

---

📋 Input Features

The model uses the following employee information:

- City
- City Development Index
- Gender
- Relevant Experience
- Enrolled University
- Education Level
- Major Discipline
- Years of Experience
- Company Size
- Company Type
- Last New Job
- Training Hours

---

📊 Prediction Output

The application predicts:

- ✅ Employee is likely to stay
- ⚠️ Employee is likely to change jobs

It also displays:

- Prediction confidence
- Stay probability chart
- Job change probability chart

---

📸 User Interface

The application includes:

- Beautiful gradient background
- Professional hero banner
- Organized employee information form
- Color-coded prediction results
- Interactive probability visualizations

---

👨‍💻 Author

Shreya Shende

GitHub: https://github.com/shreyashende2005-afk

---

⭐ Support

If you found this project helpful, please give this repository a ⭐ on GitHub.
