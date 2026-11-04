import csv, pandas as pd

# Remove corrupted lines
bad_lines_log = []

def handle_bad_line(line_parts):
    bad_lines_log.append(line_parts)
    return None

df = pd.read_csv("raw_data/2014_data.csv", encoding="latin1", on_bad_lines=handle_bad_line, engine="python")

# Keep only a select few data columns
df_cleaned = df[["domain", "label"]]
df_cleaned.to_csv("processed_data/2014_data_cleaned.csv", index=False)