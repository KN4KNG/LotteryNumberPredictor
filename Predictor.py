import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from random import randint

i = 0
while i < 10: 
    # Load the data from Excel file
    data = pd.read_excel("previous_data.xlsx")

    # Split the data into features (X) and target (y)
    X = data[['1st_number', '2nd_number', '3rd_number', '4th_number', '5th_number', '6th_number']]
    y = data.iloc[:, 1:]

    # Train a Random Forest Regression model
    model = RandomForestRegressor(n_estimators=1000, random_state=None)
    model.fit(X, y)

    # Generate a new set of random features for prediction
    new_data = pd.DataFrame({
        "1st_number": [randint(1, 70) for _ in range(100)],
        "2nd_number": [randint(1, 70) for _ in range(100)],
        "3rd_number": [randint(1, 70) for _ in range(100)],
        "4th_number": [randint(1, 70) for _ in range(100)],
        "5th_number": [randint(1, 70) for _ in range(100)],
        "6th_number": [randint(1, 25) for _ in range(100)],
    })

    # Use the trained model to predict the next 6 numbers for each set of features
    predictions = model.predict(new_data)

    # Get the most likely set of numbers based on the predictions
    most_likely_set = predictions[0]
    for p in predictions:
        if p[0] > most_likely_set[0]:
            most_likely_set = p

    # Convert most_likely_set to whole numbers
    rounded_most_likely_set = [round(x) for x in most_likely_set]

    # Print the most likely set of numbers
    print(str(f"{i+1:02d}") + ". The most likely set of numbers is:", rounded_most_likely_set)
    i += 1
