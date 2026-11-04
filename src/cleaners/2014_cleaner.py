import pandas as pd

# Remove corrupted lines
bad_lines_log = []

def handle_bad_line(line_parts):
    bad_lines_log.append(line_parts)
    return None

df = pd.read_csv("data/raw/2014_data.csv", encoding="utf-8", encoding_errors="replace", on_bad_lines=handle_bad_line, engine="python")

# Keep only a select few data columns
df_cleaned = df[["url", "label"]]

# Filter corrupted rows
valid_web_url_pattern = r'^(?:https?://|www\.)[\x21-\x7E]+$'
df_cleaned = df_cleaned[df_cleaned["url"].str.contains(valid_web_url_pattern, regex=True, na=False, case=False)]

# Remove duplicate items
df_cleaned = df_cleaned.drop_duplicates()

# Add URL len column, remove urls longer than 1000 chars
df_cleaned["url"] = df_cleaned["url"].astype(str)
df_cleaned["url_len"] = df_cleaned["url"].str.len()

df_cleaned = df_cleaned[df_cleaned["url_len"] <= 1000]

df_cleaned.to_csv("data/processed/2014_data_cleaned.csv", index=False)
