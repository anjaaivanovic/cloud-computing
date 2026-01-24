import pandas as pd
import sys
import traceback
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import math

try:
    csv = sys.argv[1]
    column = sys.argv[2]
    train_size = float(sys.argv[3])

    if not 0 < train_size < 1:
        raise ValueError("training_set_percentage must be between 0 and 1")

    df = pd.read_csv(csv)

    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in CSV")

    X = df.drop(columns=[column])
    y = df[column]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=train_size, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    rmse = math.sqrt(mean_squared_error(y_test, preds))
    prmse = rmse / y_test.mean()

    with open("metrics.txt", "w") as f:
        f.write(f"RMSE: {rmse}\n")
        f.write(f"PRMSE: {prmse}\n")

except Exception as e:
    with open("metrics.txt", "w") as f:
        f.write("ERROR: " + str(e) + "\n")
    import sys, traceback
    traceback.print_exc()
    sys.exit(1)