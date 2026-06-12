import os
import json
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error

csv_file = os.environ["DATASET_PATH"]
column = os.environ["TARGET_COLUMN"]

fold_id = int(os.environ["FOLD_ID"])
k = int(os.environ["NUM_FOLDS"])

output_dir = os.environ.get("OUTPUT_DIR", "/output")

data = pd.read_csv(csv_file)

data = data.fillna(data.mean(numeric_only=True))

Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1

data = data[
    ~((data < (Q1 - 1.5 * IQR)) |
      (data > (Q3 + 1.5 * IQR))).any(axis=1)
]

X = data.drop(columns=[column])
y = data[column]

N = len(data)
fold_size = N // k

start = fold_id * fold_size
end = N if fold_id == k - 1 else (fold_id + 1) * fold_size

X_test = X.iloc[start:end]
y_test = y.iloc[start:end]

X_train = pd.concat([X.iloc[:start], X.iloc[end:]])
y_train = pd.concat([y.iloc[:start], y.iloc[end:]])

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

rmse = root_mean_squared_error(y_test, y_pred)
prmse = rmse / y_test.mean()

metrics = {
    "fold": fold_id,
    "rmse": rmse,
    "prmse": prmse
}

os.makedirs(output_dir, exist_ok=True)

with open(f"{output_dir}/metrics_fold_{fold_id}.json", "w") as f:
    json.dump(metrics, f)

print(json.dumps(metrics))