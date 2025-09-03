#!/usr/bin/env python3
"""HIT137 - Assignment 2 (Question 2)
Monthly temperature analytics across ALL stations and years.

Expected wide monthly format per row: one station, columns that include month names.
Detected month headers may be like: Jan, January, Jan(°C), Mean_Jan_Temp etc.
Station column: first matching one of station name candidates else column 0.
Latitude / longitude columns are ignored (never treated as temperatures).
Outputs:
  average_temp.txt
  largest_temp_range_station.txt
  temperature_stability_stations.txt
"""

import csv, glob, os, statistics

# Directory and output file constants
TEMPS_DIR = os.path.join(os.path.dirname(__file__), "temperatures")
AVG_OUT   = "average_temp.txt"
RANGE_OUT = "largest_temp_range_station.txt"
STAB_OUT  = "temperature_stability_stations.txt"
EPS = 1e-9

# Australian seasonal mapping for months
MONTHS = {
    1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",
    7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"
}
MONTH_TO_SEASON = {
    1:"Summer",2:"Summer",3:"Autumn",4:"Autumn",5:"Autumn",
    6:"Winter",7:"Winter",8:"Winter",9:"Spring",10:"Spring",11:"Spring",12:"Summer"
}

def parse_float(x):
    """Safely parse a value to float, returning None for invalid/missing values."""
    try:
        v = float(x)
        # Relaxed plausible Australian monthly (mean / max) bounds
        if -5 <= v <= 55:  # allow very cool alpine monthly means (rare negatives) and hot maxima
            return v
    except: pass
    return None

def detect_columns(header):
    """Detect station and month columns from CSV header."""
    norm = [h.lower().replace(" ", "") for h in header]

    # station column detection
    station_idx = 0
    for i, h in enumerate(norm):
        if "station" in h or "name" in h:
            station_idx = i
            break

    # month detection
    month_cols = {}
    for i, h in enumerate(norm):
        for m, name in MONTHS.items():
            if name.lower() in h:
                month_cols[m] = i
    return station_idx, month_cols

def process_all():
    """Main processing function to analyze all CSV files."""
    if not os.path.isdir(TEMPS_DIR):
        print(f"[ERROR] Directory '{TEMPS_DIR}' not found.")
        for fp in (AVG_OUT, RANGE_OUT, STAB_OUT):
            open(fp, "w").write("No data\n")
        return
    csvs = glob.glob(os.path.join(TEMPS_DIR, "*.csv"))
    if not csvs:
        print(f"[ERROR] No CSV files found in '{TEMPS_DIR}'.")
        for fp in (AVG_OUT, RANGE_OUT, STAB_OUT):
            open(fp, "w").write("No data\n")
        return

    # Data accumulators for analysis
    seasons = {s: [] for s in ["Summer","Autumn","Winter","Spring"]}
    per_station = {}

    # Process each CSV file
    for path in csvs:
        print(f"[INFO] Processing {os.path.basename(path)}")
        with open(path, "r", encoding="utf-8-sig") as f:
            reader = csv.reader(f)
            try: header = next(reader)
            except Exception:
                print(f"[WARN] Skipping empty or malformed file: {path}")
                continue
            st_col, month_cols = detect_columns(header)
            if not month_cols:
                print(f"[WARN] No month columns found in {path}")
                continue
            for row in reader:
                if not row or st_col >= len(row): continue
                station = row[st_col].strip()
                if not station: continue
                per_station.setdefault(station, [])
                for m, col in month_cols.items():
                    if col < len(row):
                        v = parse_float(row[col])
                        if v is not None:
                            per_station[station].append(v)
                            seasons[MONTH_TO_SEASON[m]].append(v)

    # 1) Seasonal averages
    with open(AVG_OUT, "w") as f:
        for s in ["Summer","Autumn","Winter","Spring"]:
            vals = seasons[s]
            if vals:
                f.write(f"{s}: {sum(vals)/len(vals):.1f}°C\n")
            else:
                f.write(f"{s}: No data\n")
    print(f"[OK] Wrote {AVG_OUT}")

    # 2) Temperature range - find stations with largest range
    ranges = {st: (max(v)-min(v), max(v), min(v)) for st,v in per_station.items() if len(v)>=2}
    if not ranges:
        open(RANGE_OUT, "w").write("No station data with sufficient range\n")
        print(f"[WARN] No station data with sufficient range.")
    else:
        max_range = max(r[0] for r in ranges.values())
        winners = [st for st,(rg,_,_) in ranges.items() if abs(rg-max_range)<EPS]
        with open(RANGE_OUT, "w") as f:
            for st in sorted(winners):
                rg, mx, mn = ranges[st]
                f.write(f"{st}: Range {rg:.1f}°C (Max: {mx:.1f}°C, Min: {mn:.1f}°C)\n")
        print(f"[OK] Wrote {RANGE_OUT}")

       # 3) Temperature stability (std dev)
    stabilities = {}
    for st, vals in per_station.items():
        if len(vals) >= 2:
            stabilities[st] = statistics.pstdev(vals)

    if not stabilities:
        open(STAB_OUT, "w").write("No station data with sufficient variability\n")
        print(f"[WARN] No station data with sufficient variability.")
    else:
        min_std = min(stabilities.values())
        max_std = max(stabilities.values())
        most_stable = [st for st,sd in stabilities.items() if abs(sd-min_std)<EPS]
        most_variable = [st for st,sd in stabilities.items() if abs(sd-max_std)<EPS]

        with open(STAB_OUT, "w") as f:
            for st in sorted(most_stable):
                f.write(f"Most Stable: {st}: StdDev {min_std:.1f}°C\n")
            for st in sorted(most_variable):
                f.write(f"Most Variable: {st}: StdDev {max_std:.1f}°C\n")
        print(f"[OK] Wrote {STAB_OUT}")

if __name__ == "__main__":
    process_all()







































