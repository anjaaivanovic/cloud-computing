import sys
import json
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error

csv_file = sys.argv[1]
column = sys.argv[2]
fold_id = int(sys.argv[3])
k = int(sys.argv[4])

data = pd.read_csv(csv_file)

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

with open("metrics.json", "w") as f:
    json.dump([rmse, prmse], f)