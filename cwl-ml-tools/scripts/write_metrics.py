#!/usr/bin/env python3

import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--rmse", type=float, nargs="+", required=True)
parser.add_argument("--prmse", type=float, nargs="+", required=True)
parser.add_argument("--out", default="metrics.json")

args = parser.parse_args()

data = {
    "rmse_per_fold": args.rmse,
    "prmse_per_fold": args.prmse
}

with open(args.out, "w") as f:
    json.dump(data, f, indent=2)