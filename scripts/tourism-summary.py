import pandas as pd

# Load data
df = pd.read_csv('data/gb-tourism.csv')

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Clean land column - remove commas and convert to numeric
df['by_land'] = pd.to_numeric(df['by_land'].astype(str).str.replace(',', ''), errors='coerce')
df['total'] = pd.to_numeric(df['total'].astype(str).str.replace(',', ''), errors='coerce')

# Basic summary
print("=== Gibraltar Tourism Summary ===")
print(f"Years covered: {df['year'].min()} - {df['year'].max()}")
print(f"Total records: {len(df)}")
print(f"\nPeak year (total visitors):")
peak = df.loc[df['total'].idxmax()]
print(f"  {int(peak['year'])} — {int(peak['total']):,} visitors")
print(f"\nLowest year (total visitors):")
low = df.loc[df['total'].idxmin()]
print(f"  {int(low['year'])} — {int(low['total']):,} visitors")
print(f"\nCOVID impact:")
print(f"  2019: {int(df[df['year']==2019]['total'].values[0]):,}")
print(f"  2020: {int(df[df['year']==2020]['total'].values[0]):,}")
print(f"\nLast 5 years:")
print(df.tail(5)[['year','by_air','by_sea','by_land','total']].to_string(index=False))
