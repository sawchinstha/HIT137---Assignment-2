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

def detect_columns(header): # iterates through each string in the header list
    """Detect station and month columns from CSV header."""
    norm = [h.lower().replace(" ", "") for h in header] #converts the current header string (h) to lowercase and removes any spaces from the lowercase string

    # station column detection
    station_idx = 0 # initializes a variable station_idx to 0
    for i, h in enumerate(norm): #  loop iterates through the norm list
        if "station" in h or "name" in h: # checks if the substring "station" is present in the header string also if the substring "name" is present
            station_idx = i # If a match is found, the current index i is assigned to station_idx
            break

    # month detection
    month_cols = {} #  empty dictionary month_cols is initialized
    for i, h in enumerate(norm): # iterates through the list of normalized header strings
        for m, name in MONTHS.items(): # iterates through the MONTHS dictionary 
            if name.lower() in h: # checks if the lowercase version of the full month name is a substring of the current normalized header 
                month_cols[m] = i # If a match is found, the month number m is added to the month_cols dictionary as a key, and its corresponding column index i is assigned as the value
    return station_idx, month_cols # function returns two values which contains a mapping of months to their column indices

def process_all():
    """Main processing function to analyze all CSV files."""
    if not os.path.isdir(TEMPS_DIR): # checks if the path provided by variable is a valid directory
        print(f"[ERROR] Directory '{TEMPS_DIR}' not found.")
        for fp in (AVG_OUT, RANGE_OUT, STAB_OUT): #  creates three output files (AVG_OUT, RANGE_OUT, STAB_OUT) and writes "No data" into each of them
            open(fp, "w").write("No data\n")
        return
    csvs = glob.glob(os.path.join(TEMPS_DIR, "*.csv")) # creates a valid file path string that combines the directory name with the search pattern (.csv)
    if not csvs: #  checks if the csvs list is empty
        print(f"[ERROR] No CSV files found in '{TEMPS_DIR}'.")
        for fp in (AVG_OUT, RANGE_OUT, STAB_OUT):
            open(fp, "w").write("No data\n")
        return

    # Data accumulators for analysis
    seasons = {s: [] for s in ["Summer","Autumn","Winter","Spring"]}
    per_station = {}

    # Process each CSV file
    for path in csvs: # loop starts the file processing for each CSV file found
        print(f"[INFO] Processing {os.path.basename(path)}") 
        with open(path, "r", encoding="utf-8-sig") as f: # opens the CSV file for reading.
            reader = csv.reader(f) # creates a csv.reader object which makes it easy to iterate over rows in the CSV file
            try: header = next(reader)
            except Exception:
                print(f"[WARN] Skipping empty or malformed file: {path}")
                continue
            st_col, month_cols = detect_columns(header) # calls a function to get the index of the station column (st_col) and a dictionary of month columns
            if not month_cols: # finds no month columns, it prints a warning and skips the file
                print(f"[WARN] No month columns found in {path}")
                continue
            for row in reader:
                if not row or st_col >= len(row): continue
                station = row[st_col].strip() #  extracts the station name from the station column and removes any leading/trailing whitespace
                if not station: continue # Skips the row if the station name is empty
                per_station.setdefault(station, []) # It checks if station is a key in the per_station dictionary and if it's not, it creates the key and sets its value to an empty list
                for m, col in month_cols.items(): # iterates through the months that were found in the header
                    if col < len(row): # checks if the current row has a column for the month being processed
                        v = parse_float(row[col]) # likely handles non-numeric values by returning None
                        if v is not None: # checks if the value was successfully converted to a number
                            per_station[station].append(v) # If the value is valid, it's added to the list of temperatures for the current station
                            seasons[MONTH_TO_SEASON[m]].append(v)

    # 1) Seasonal averages
    with open(AVG_OUT, "w") as f: # If the file already exists, its contents will be completely erased & if it doesn't exist, a new, empty file will be created
        for s in ["Summer","Autumn","Winter","Spring"]: # iterates through a fixed list of season names in a specific order
            vals = seasons[s] # it retrieves the list of all collected temperature values from the seasons dictionary and assigns it to the vals variable for each season
            if vals: # checks if the vals list is not empty
                f.write(f"{s}: {sum(vals)/len(vals):.1f}°C\n") # runs if data exists for the season
            else:
                f.write(f"{s}: No data\n")
    print(f"[OK] Wrote {AVG_OUT}")

    # 2) Temperature range - find stations with largest range
    ranges = {st: (max(v)-min(v), max(v), min(v)) for st,v in per_station.items() if len(v)>=2} # calculate the temperature range for every station
    if not ranges: # checks if the ranges dictionary is empty
        open(RANGE_OUT, "w").write("No station data with sufficient range\n")
        print(f"[WARN] No station data with sufficient range.")
    else:
        max_range = max(r[0] for r in ranges.values()) # finds the single largest range value from the ranges dictionary
        winners = [st for st,(rg,_,_) in ranges.items() if abs(rg-max_range)<EPS] # identifies all stations whose calculated range is approximately equal to max_range
        with open(RANGE_OUT, "w") as f: # output file (RANGE_OUT) is opened in write mode
            for st in sorted(winners): # code iterates through the winners list, which is sorted alphabetically to ensure consistent output
                rg, mx, mn = ranges[st] # unpacks the tuple of range, max, and min values for the current winning station.
                f.write(f"{st}: Range {rg:.1f}°C (Max: {mx:.1f}°C, Min: {mn:.1f}°C)\n") # ormatted string is written to the file
        print(f"[OK] Wrote {RANGE_OUT}")

   # 3) Temperature stability (std dev)
    stabilities = {} # empty dictionary is initialized to store the standard deviation for each station
    for st, vals in per_station.items(): # loops through the per_station dictionary, which contains lists of temperature values (vals) for each station (st)
        if len(vals) >= 2: # this check ensures that a calculation is possible
            stabilities[st] = statistics.pstdev(vals) # calculates the population standard deviation of the temperature values using Python's statistics.pstdev() function and stores the result in the stabilities dictionary

    if not stabilities: # checks if the stabilities dictionary is empty.
        open(STAB_OUT, "w").write("No station data with sufficient variability\n")
        print(f"[WARN] No station data with sufficient variability.")
    else:
        min_std = min(stabilities.values()) # Finds the lowest standard deviation value, representing the most stable temperature
        max_std = max(stabilities.values()) # Finds the highest standard deviation value, representing the most variable temperature
        most_stable = [st for st,sd in stabilities.items() if abs(sd-min_std)<EPS] # finds all stations whose standard deviation is equal to the minimum
        most_variable = [st for st,sd in stabilities.items() if abs(sd-max_std)<EPS] # finds all stations with the maximum standard deviation

        with open(STAB_OUT, "w") as f: # it will either create a new file or overwrite any existing one
            for st in sorted(most_stable): # iterates through the most_stable list, which contains the names of the stations with the lowest temperature standard deviation
                f.write(f"Most Stable: {st}: StdDev {min_std:.1f}°C\n")
            for st in sorted(most_variable): # for the stations with the highest temperature variability
                f.write(f"Most Variable: {st}: StdDev {max_std:.1f}°C\n")
        print(f"[OK] Wrote {STAB_OUT}")
    if not stabilities:
        open(STAB_OUT, "w").write("No station data with sufficient variability\n")
        print(f"[WARN] No station data with sufficient variability.")
    else:
        min_std = min(stabilities.values()) # finds the smallest standard deviation value, representing the most stable temperature
        max_std = max(stabilities.values()) # finds the largest standard deviation value, representing the most variable temperature
        most_stable = [st for st,sd in stabilities.items() if abs(sd-min_std)<EPS] # creates a list of all stations that have a standard deviation approximately equal to the minimum.
        most_variable = [st for st,sd in stabilities.items() if abs(sd-max_std)<EPS] # creates a list of all stations that have a standard deviation approximately equal to the maximum

        with open(STAB_OUT, "w") as f: # opens the designated file for writing, overwriting any previous content
            for st in sorted(most_stable):
                f.write(f"Most Stable: {st}: StdDev {min_std:.1f}°C\n")
            for st in sorted(most_variable):
                f.write(f"Most Variable: {st}: StdDev {max_std:.1f}°C\n")
        print(f"[OK] Wrote {STAB_OUT}")
if __name__ == "__main__": # ensures that  process_all() function is only called when the script is run directly
    process_all()







































