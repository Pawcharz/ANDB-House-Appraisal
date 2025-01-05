import pandas as pd
from datetime import datetime

file_path = 'realtor.csv'  
df = pd.read_csv(file_path)

df = df.dropna(subset=['bed', 'bath'])

df['prev_sold_date'] = pd.to_datetime(df['prev_sold_date'], errors='coerce')

current_date = datetime.now()
df = df[df['prev_sold_date'] <= current_date]

rows_to_remove = len(df) // 4  
df = df.iloc[:-rows_to_remove]  

cleaned_file_path = 'cleaned_dataset.csv'
df.to_csv(cleaned_file_path, index=False)

print(f"Dataset cleaned and saved to {cleaned_file_path}")