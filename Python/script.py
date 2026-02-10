
# every day we get a CSV file with the previous day’s data in the format country_YESTERDAY_DATE. 
# The CSV file contains country names and product IDs. 
# Assume the country column initially has only 4 countries. 
# Calculate total trips for per product_id from each file?

import pandas as pd
import glob
import os

input_path = "/home/nineleaps/Downloads/NineLeaps/Python/Data/*.csv"
output_path = "/home/nineleaps/Downloads/NineLeaps/Python/Output/master_file.csv"

all_data = []

for file in glob.glob(input_path):
    df = pd.read_csv(file)
    date = os.path.basename(file).split('_')[1].replace(".csv","")
    df['file_date'] = date  # Add date column to dataframe
    all_data.append(df)

combined_df = pd.concat(all_data,ignore_index= True)

result = (

    combined_df
    .groupby(["file_date","product_id"])
    .size()
    .reset_index(name = "total_trips")
)

result.to_csv(output_path,index=False)

print(output_path)
