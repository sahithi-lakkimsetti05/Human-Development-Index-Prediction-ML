\# 🌍 Human Development Index (HDI) Prediction using Machine Learning



\## 📌 Project Overview



The Human Development Index (HDI) is a statistical measure developed to evaluate the development level of countries based on important factors such as health, education, and income.



This project focuses on developing a Machine Learning model that predicts the \*\*HDI Score\*\* of a country using major human development indicators.



The project uses a \*\*Linear Regression Machine Learning algorithm\*\* to learn the relationship between development indicators and HDI Score.



The trained model is saved using \*\*Pickle\*\* and deployed using a \*\*Flask Web Application\*\*, where users can enter development indicator values and get predicted HDI scores instantly.



\---



\# 🎯 Project Aim



The main aim of this project is:



To develop a Machine Learning-based web application that predicts the Human Development Index (HDI) Score using:



\- Life Expectancy

\- Expected Years of Schooling

\- Mean Years of Schooling

\- GNI per Capita



\---



\# 🚀 Project Workflow



```

Dataset Collection

&#x20;       |

&#x20;       ↓

Data Loading

&#x20;       |

&#x20;       ↓

Data Cleaning

&#x20;       |

&#x20;       ↓

Data Preprocessing

&#x20;       |

&#x20;       ↓

Exploratory Data Analysis (EDA)

&#x20;       |

&#x20;       ↓

Feature Selection

&#x20;       |

&#x20;       ↓

Train-Test Split

&#x20;       |

&#x20;       ↓

Machine Learning Model Training

&#x20;       |

&#x20;       ↓

Model Evaluation

&#x20;       |

&#x20;       ↓

Model Saving using Pickle

&#x20;       |

&#x20;       ↓

Flask Web Application Deployment

&#x20;       |

&#x20;       ↓

HDI Score Prediction

```



\---



\# 📂 Dataset Information



\## Dataset Used



\*\*HDI.xlsx\*\*



The dataset contains Human Development Index information of different countries.



\## Dataset Features



| Feature | Description |

|---|---|

| Life Expectancy | Average number of years a person is expected to live |

| Expected Years of Schooling | Expected duration of education |

| Mean Years of Schooling | Average completed education years |

| GNI per Capita | Gross National Income per person |



\## Target Variable



```

HDI Score

```



\---



\# 🧹 Data Preprocessing



The following preprocessing steps were performed:



\## 1. Dataset Loading



The HDI Excel dataset was loaded using Pandas.



```python

pd.read\_excel()

```



\---



\## 2. Column Renaming



Original dataset columns were renamed for better understanding.



| Original Column | New Column |

|---|---|

| Value | HDI Score |

| (years) | Life Expectancy |

| (years).1 | Expected Years of Schooling |

| (years).2 | Mean Years of Schooling |

| (2021 PPP $) | GNI per Capita |



\---



\## 3. Removing Unnecessary Data



Removed:



\- Empty rows

\- Regional classifications

\- Development category groups



Examples removed:



\- World

\- South Asia

\- Europe and Central Asia

\- Very High Human Development

\- Developing Countries



\---



\## 4. Handling Missing Values



Missing values in independent variables were handled using mean replacement.



```python

X = X.fillna(X.mean())

```



Rows with missing HDI Score values were removed.



\---



\# 📊 Exploratory Data Analysis (EDA)



EDA was performed to understand relationships between development indicators and HDI Score.



\## 1. Mean Years of Schooling vs HDI Score



Visualization:



\*\*Strip Plot\*\*



Purpose:



\- Analyze the relationship between education level and HDI.



\---



\## 2. Life Expectancy vs HDI Score



Visualization:



\*\*Strip Plot\*\*



Purpose:



\- Understand the influence of health factors on HDI.



\---



\## 3. Correlation Heatmap



Correlation analysis was performed between:



\- HDI Score

\- Life Expectancy

\- Expected Years of Schooling

\- Mean Years of Schooling

\- GNI per Capita





\### Observations:



\- Life Expectancy has a strong positive correlation with HDI.

\- Mean Years of Schooling strongly influences HDI.

\- GNI per Capita contributes significantly to HDI.



\---



\# 🤖 Machine Learning Model



\## Algorithm Used



\### Linear Regression



Linear Regression was selected because:



\- HDI Score is a continuous numerical value.

\- The model identifies relationships between input indicators and HDI Score.



\---



\# 📌 Feature Selection



\## Independent Variables (X)



```

Life Expectancy



Expected Years of Schooling



Mean Years of Schooling



GNI per Capita

```



\## Dependent Variable (Y)



```

HDI Score

```



\---



\# ✂️ Train-Test Split



The dataset was divided into:



\### Training Data



80%



\### Testing Data



20%



Using:



```python

train\_test\_split()

```



Dataset after preprocessing:



```

X Shape : (193,4)



Y Shape : (193,)

```



\---



\# 🏋️ Model Training



Linear Regression model was trained using:



```python

from sklearn.linear\_model import LinearRegression



model = LinearRegression()



model.fit(X\_train,Y\_train)

```



The model learned the relationship between human development indicators and HDI Score.



\---



\# 📈 Model Evaluation



The trained model was evaluated using:



\## R² Score



Obtained R² Score:



```

0.971612

```



The model explains approximately \*\*97% of the variation in HDI Score\*\*, showing good prediction performance.



\---



\# 🔮 HDI Prediction



The trained model was tested using unseen data.



Example prediction:



| Actual HDI | Predicted HDI |

|---|---|

| 0.649 | 0.646 |

| 0.798 | 0.780 |

| 0.622 | 0.624 |



The predicted values were close to actual values.



\---



\# 💾 Model Saving using Pickle



The trained machine learning model was saved using Pickle.



Generated file:



```

hdi\_model.pkl

```



Pickle converts the trained model object into a file so that it can be loaded later without retraining.



\---



\# 🌐 Flask Web Application



A Flask web application was created to deploy the trained Machine Learning model.



The Flask application performs:



\- Loading the saved model

\- Accepting user inputs

\- Passing inputs to the ML model

\- Predicting HDI Score

\- Displaying the result



\---

\# 📸 Application Output



The following screenshots demonstrate the Exploratory Data Analysis (EDA) visualizations and the deployed Flask web application.



\---



\## 📊 Mean Years of Schooling vs HDI Score



This strip plot shows the relationship between \*\*Mean Years of Schooling\*\* and the \*\*HDI Score\*\*.



!\[Mean Years vs HDI](images/mean\_years\_vs\_hdi.png)



\---



\## 📊 Life Expectancy vs HDI Score



This strip plot illustrates the relationship between \*\*Life Expectancy\*\* and the \*\*HDI Score\*\*.



!\[Life Expectancy vs HDI](images/life\_expectancy\_vs\_hdi.png)



\---



\## 📊 Correlation Heatmap



The heatmap displays the correlation among the selected Human Development indicators.



!\[Correlation Heatmap](images/correlation\_heatmap.png)



\---



\## 🌐 Flask Web Application Interface



The web application provides a simple and user-friendly interface where users can enter the required development indicators to predict the HDI Score.



!\[HDI Interface](images/hdi\_interface.png)



\---



\## 🎯 HDI Prediction Result



After entering valid input values, the application predicts the \*\*Human Development Index (HDI) Score\*\* using the trained Linear Regression model.



!\[HDI Prediction](images/hdi\_prediction.png)



\---

\---



\## 🎯 HDI Prediction Result



!\[HDI Prediction](images/hdi\_prediction.png)



\---



\# 🖥️ Web Application Features



The application provides:



✅ User-friendly interface  

✅ Input fields for development indicators  

✅ Real-time HDI prediction  

✅ Machine Learning based estimation  



\---





\# 📁 Project Structure



```

Human-Development-Index-Prediction-ML



│

├── Dataset

│   └── HDI.xlsx

│

├── Flask

│   │

│   ├── flask\_app.py

│   ├── hdi\_model.pkl

│   │

│   ├── templates

│   │   └── index.html

│   │

│   └── static

│       └── css

│           └── style.css

│

├── images

│   ├── hdi\_interface.png

│   └── hdi\_prediction.png

│

├── app.py

│

├── requirements.txt

│

└── README.md

```



\---



\# ⚙️ Installation



\## Clone Repository



```bash

git clone <repository-url>

```



\## Navigate into Project Folder



```bash

cd Human-Development-Index-Prediction-ML

```



\## Create Virtual Environment



```bash

python -m venv .venv

```



\## Activate Environment



Windows:



```bash

.venv\\Scripts\\activate

```



\## Install Required Libraries



```bash

pip install -r requirements.txt

```



\---



\# ▶️ Running the Project



\## Step 1: Train Machine Learning Model



Run:



```bash

python app.py

```



This creates:



```

hdi\_model.pkl

```



\---



\## Step 2: Run Flask Application



Move into Flask folder:



```bash

cd Flask

```



Run:



```bash

python flask\_app.py

```



Open browser:



```

http://127.0.0.1:5000/

```



\---



\# 🛠️ Technologies Used



| Technology | Purpose |

|---|---|

| Python | Programming Language |

| Pandas | Data Processing |

| NumPy | Numerical Operations |

| Matplotlib | Data Visualization |

| Seaborn | Statistical Visualization |

| Scikit-Learn | Machine Learning |

| Flask | Web Deployment |

| Pickle | Model Serialization |

| HTML | Frontend Structure |

| CSS | User Interface Design |



\---



\# 🔮 Future Improvements



Possible improvements:



\- Try advanced Machine Learning algorithms:

&#x20; - Random Forest

&#x20; - XGBoost

&#x20; - Gradient Boosting



\- Add database integration



\- Deploy application using:

&#x20; - Render

&#x20; - AWS

&#x20; - Azure



\- Add interactive dashboards and charts



\---



\# 👨‍💻 Author



\*\*RAVI VENKATA PUSHPA LATHA\*\*



Machine Learning Project  

\*\*Human Development Index Prediction\*\*



