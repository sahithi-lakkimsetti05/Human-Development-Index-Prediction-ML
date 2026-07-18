import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load Excel file
df = pd.read_excel("Dataset/HDI.xlsx", header=5)


# Rename columns
df.rename(columns={
    "Value": "HDI Score",
    "(years)": "Life Expectancy",
    "(years).1": "Expected Years of Schooling",
    "(years).2": "Mean Years of Schooling",
    "(2021 PPP $)": "GNI per Capita"
}, inplace=True)


# Remove empty rows
df = df.dropna(subset=["Country", "HDI Score"])


# Convert numeric columns
numeric_columns = [
    "HDI Score",
    "Life Expectancy",
    "Expected Years of Schooling",
    "Mean Years of Schooling",
    "GNI per Capita"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")


# Remove unnecessary columns
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]


# -------------------------------
# Remove Regional Entries
# -------------------------------


remove_regions = [
    "Arab States",
    "East Asia and the Pacific",
    "Europe and Central Asia",
    "Latin America and the Caribbean",
    "South Asia",
    "Sub-Saharan Africa",
    "Least developed countries",
    "Small island developing states",
    "Organisation for Economic Co-operation and Development",
    "World",
    "Very high human development",
    "High human development",
    "Medium human development",
    "Low human development",
    "Developing countries"
]



df = df[~df["Country"].isin(remove_regions)]


# -------------------------------
# Dataset Information
# -------------------------------

print(df.head())

print("\nColumns:")
print(df.columns)

print("\nDataset Size:")
print(df.shape)


# -------------------------------
# Unique Country Values
# -------------------------------

unique_countries = df["Country"].unique()

print("\nUnique Countries:")
print(unique_countries)

print("\nTotal unique countries:", df["Country"].nunique())

print("Duplicate countries:", df["Country"].duplicated().sum())


# -------------------------------
# Mean Years of Schooling vs HDI
# Strip Plot
# -------------------------------

# Select first 20 rows to avoid overcrowding
data1 = df.head(20)


plt.figure(figsize=(10, 6))

sns.stripplot(
    data=data1,
    x="Mean Years of Schooling",
    y="HDI Score",
    size=8
)

plt.title("Mean Years of Schooling vs HDI Score")
plt.xlabel("Mean Years of Schooling")
plt.ylabel("HDI Score")

plt.show()



# -------------------------------
# Life Expectancy vs HDI Score
# Strip Plot
# -------------------------------

plt.figure(figsize=(10, 6))

sns.stripplot(
    data=data1,
    x="Life Expectancy",
    y="HDI Score",
    size=8
)

plt.title("Life Expectancy vs HDI Score")
plt.xlabel("Life Expectancy (Years)")
plt.ylabel("HDI Score")

plt.xticks(rotation=45)

plt.show()
# -------------------------------
# Correlation Heatmap
# -------------------------------

# Select numerical features
corr_columns = [
    "HDI Score",
    "Life Expectancy",
    "Expected Years of Schooling",
    "Mean Years of Schooling",
    "GNI per Capita"
]

corr_data = df[corr_columns]


# Create correlation matrix
correlation_matrix = corr_data.corr()

print("\nCorrelation Matrix:")
print(correlation_matrix)


# Plot heatmap
plt.figure(figsize=(10, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap of Human Development Indicators")
plt.show()
# -------------------------------
# Select Features and Target
# -------------------------------

# Independent Variables (X)
X = df[
    [
        "Life Expectancy",
        "Expected Years of Schooling",
        "Mean Years of Schooling",
        "GNI per Capita"
    ]
]


# Dependent Variable (Y) - Target
Y = df["HDI Score"]
# -------------------------------
# Remove Null Values in Target Y
# -------------------------------

data = pd.concat([X, Y], axis=1)

# Remove rows where HDI Score is missing
data = data.dropna(subset=["HDI Score"])

# Split again
X = data.drop("HDI Score", axis=1)
Y = data["HDI Score"]

print("\nNull Values in Y:")
print(Y.isnull().sum())

print("New X Shape:", X.shape)
print("New Y Shape:", Y.shape)

#----------------------------------
# Display features and target
#-----------------------------------
print("\nIndependent Variables (X):")
print(X.head())

print("\nDependent Variable (Y):")
print(Y.head())


# Check shapes
print("\nX Shape:", X.shape)
print("Y Shape:", Y.shape)
# -------------------------------
# Check Null Values in Input Features
# -------------------------------

print("\nNull Values in Independent Variables (X):")

print(X.isnull().sum())
# -------------------------------
# Fill Null Values in X
# -------------------------------

# Replace missing values with column mean
X = X.fillna(X.mean())

# Check null values after filling
print("\nNull Values After Filling:")
print(X.isnull().sum())
# -------------------------------
# Train-Test Split
# -------------------------------

from sklearn.model_selection import train_test_split

# Split dataset into training and testing data
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

# Display shapes of train and test data
print("\nTraining Data:")
print("X_train shape:", X_train.shape)
print("Y_train shape:", Y_train.shape)

print("\nTesting Data:")
print("X_test shape:", X_test.shape)
print("Y_test shape:", Y_test.shape)
# -------------------------------
# Linear Regression Model Training
# -------------------------------

from sklearn.linear_model import LinearRegression

# Check null values before training
print("\nNull values in Y_train:")
print(Y_train.isnull().sum())

# Create Linear Regression model
model = LinearRegression()

# Train the model using training data
model.fit(X_train, Y_train)
# Save trained model
import pickle

with open("hdi_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("hdi_model.pkl created successfully")

print("\nLinear Regression Model Training Completed")
# -------------------------------
# Generate HDI Predictions
# -------------------------------

# Predict HDI Score using test data
y_pred = model.predict(X_test)

print("\nPredicted HDI Values (y_pred):")
print(y_pred)


# -------------------------------
# Calculate R-Squared Value
# -------------------------------

from sklearn.metrics import r2_score

r2 = r2_score(Y_test, y_pred)

print("\nR-Squared Value (R2 Score):")
print(r2)


# -------------------------------
# Inspect Actual y_test Values
# -------------------------------

print("\nActual HDI Values (y_test):")
print(Y_test.values)


# -------------------------------
# Compare y_test and y_pred
# -------------------------------

comparison = pd.DataFrame({
    "Actual HDI": Y_test.values,
    "Predicted HDI": y_pred
})

print("\nActual vs Predicted HDI:")
print(comparison.head(10))


# -------------------------------
# Test Model with Fewer Values
# -------------------------------

# Select first 3 test samples
sample_input = X_test.head(3)

sample_prediction = model.predict(sample_input)

print("\nPredictions for First 3 Test Values:")
print(sample_prediction)
# -------------------------------
# Save Trained Model using Pickle
# -------------------------------

import pickle

# Save the trained model
with open("hdi_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nModel saved successfully as hdi_model.pkl")