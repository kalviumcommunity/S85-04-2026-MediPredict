"""Demo data script: simple data operations and console output.

Run: python scripts/demo_data_script.py

This script reads `data/raw/sample.csv` if present, otherwise uses a small built-in sample.
It computes simple summaries and prints them to the console to demonstrate script execution flow.
"""
from __future__ import annotations
import csv
import os
from statistics import mean
from typing import List, Dict, Tuple


def read_data(path: str = os.path.join("data", "raw", "sample.csv")) -> Tuple[List[Dict[str, object]], str]:
    """Read CSV data if available, otherwise return a built-in sample.

    Returns tuple (data, source) where data is a list of records and source is 'file' or 'builtin'.
    """
    if os.path.exists(path):
        data: List[Dict[str, object]] = []
        with open(path, newline="", encoding="utf8") as fh:
            reader = csv.DictReader(fh)
            for r in reader:
                data.append({
                    "date": r.get("date"),
                    "total_patients": int(r.get("total_patients", 0)),
                    "oxygen_usage": float(r.get("oxygen_usage", 0.0)),
                    "ICU_cases": int(r.get("ICU_cases", 0)),
                })
        return data, "file"

    # fallback built-in sample (keeps script self-contained)
    data = [
        {"date": "2026-04-01", "total_patients": 45, "oxygen_usage": 120.5, "ICU_cases": 5},
        {"date": "2026-04-02", "total_patients": 52, "oxygen_usage": 135.2, "ICU_cases": 6},
        {"date": "2026-04-03", "total_patients": 48, "oxygen_usage": 128.0, "ICU_cases": 4},
        {"date": "2026-04-04", "total_patients": 60, "oxygen_usage": 150.8, "ICU_cases": 8},
        {"date": "2026-04-05", "total_patients": 55, "oxygen_usage": 142.3, "ICU_cases": 7},
    ]
    return data, "builtin"


def summarize(data: List[Dict[str, object]]) -> Dict[str, object]:
    """Compute simple summaries from the dataset."""
    total_patients_sum = sum(int(d["total_patients"]) for d in data)
    avg_oxygen = mean(float(d["oxygen_usage"]) for d in data)
    total_icu = sum(int(d["ICU_cases"]) for d in data)
    high_icu_dates = [d["date"] for d in data if int(d["ICU_cases"]) >= 7]

    return {
        "num_records": len(data),
        "total_patients_sum": total_patients_sum,
        "avg_oxygen": round(avg_oxygen, 2),
        "total_icu": total_icu,
        "high_icu_dates": high_icu_dates,
    }


def main() -> None:
    """Script entry point: read, summarize, and print results with brief execution notes."""
    data, source = read_data()
    summary = summarize(data)

    print(f"Data source: {source}")
    print(f"Records: {summary['num_records']}")
    print(f"Total patients (sum): {summary['total_patients_sum']}")
    print(f"Average oxygen usage: {summary['avg_oxygen']}")
    print(f"Total ICU cases: {summary['total_icu']}")
    print("Dates with high ICU cases (>=7):")
    if summary["high_icu_dates"]:
        for d in summary["high_icu_dates"]:
            print(" -", d)
    else:
        print(" - None")

    print("\nExecution flow: read_data() -> summarize() -> print outputs")


if __name__ == "__main__":
    main()
