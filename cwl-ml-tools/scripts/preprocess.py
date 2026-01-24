import pandas as pd
import sys

input_csv = sys.argv[1]

df = pd.read_csv(input_csv)

df = df.fillna(df.mean(numeric_only=True))

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

df = df[~((df < (Q1 - 1.5 * IQR)) |
          (df > (Q3 + 1.5 * IQR))).any(axis=1)]

df.to_csv("processed.csv", index=False)

import os
print("Current working directory:", os.getcwd())
print("Files here:", os.listdir())
