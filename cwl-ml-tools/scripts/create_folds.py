import sys
import json

k = sys.argv[1]

folds = list(range(int(k)))
with open("folds.json", "w") as f:
    json.dump(folds, f)