# 🚢 Titanic Survival Prediction - Logistic Regression Model

Welcome to the `titanic_model` repository!  
This project uses a **Logistic Regression** model to predict whether a passenger would survive the Titanic disaster, based on features like **age, sex, and port of embarkation**.

---

## 📌 Key Features

- Cleaned and preprocessed Titanic dataset using Pandas.
- Converted categorical features (`Sex`, `Embarked`) into numeric values.
- Handled missing values in `Age` and `Embarked` columns.
- Trained a simple **Logistic Regression** model using scikit-learn.
- Frontend is pretty ugly but I could'nt improve as I am not a frontend developer

---

## 🧠 Machine Learning Details

| Component | Description |
|----------|-------------|
| **Algorithm** | Logistic Regression |
| **Libraries Used** | Pandas, NumPy, scikit-learn |
| **Target Variable** | `Survived` (0 = No, 1 = Yes) |


---

## 📊 Dataset Overview

- **Source:** [Kaggle Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic/data)
- **Important Columns Used:**
  - `Age`: Missing values filled with mean age.
  - `Sex`: Converted to binary (`male` → 0, `female` → 1).
  - `Embarked`: Missing values filled with `'S'`, mapped as `'S' → 0`, `'C' → 1`, `'Q' → 2`.

---

## 🧪 How to Run

 Run Locally

```bash
git clone https://github.com/yourusername/titanic_model.git
cd titanic_model
python titanic_model.py
```



---

## 🛠️ Folder Structure

```
titanic_model/
│
├── titanic_model.py         # Main Python script
├── titanic.csv              # Dataset (if included)
├── README.md                # This file
└── requirements.txt         # (Optional) dependencies
```

---

## 🚀 Future Scope

- Add more ML models (Random Forest, Decision Trees).
- Deploy using Streamlit or Flask (UI-ready version).
- Improve feature engineering and tuning.

---

## 👨‍💻 Author

**Ishaan Jha**  
📍 Student | ML & AI Enthusiast  
🌐 [GitHub](https://github.com/ishaanjha23)  
🧠 Goal: Build an AI Startup by 18 years of age 🚀

---
\
