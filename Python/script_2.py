import pandas as pd
import glob
import os
import pycountry
from datetime import datetime, timedelta

file_path = "/home/nineleaps/Downloads/NineLeaps/Python/Data_2/*.csv"
output_path = "/home/nineleaps/Downloads/NineLeaps/Python/output_2"

yesterday = (datetime.now()-timedelta(days=1)).strftime("%Y-%m-%d")
print(yesterday)



all_data = []
for file in glob.glob(file_path):


    date            = os.path.basename(file).split("_")[1].replace(".csv","")
    if date == yesterday:
        df              = pd.read_csv(file)
        country         = os.path.basename(file).split("_")[0].lower()
        df["file_date"] = date
        df["country"]   = country  
        all_data.append(df)

if all_data:
        
    combined_df = pd.concat(all_data,ignore_index=True)


    result = (
                combined_df
                .groupby(["file_date","country","product_id"])
                .size()
                .reset_index(name = "total_trips")

    )

    result.to_csv(output_path+"/master.csv")
    print("Files written to master_csv. Please check")
else:
    print("no files exist")