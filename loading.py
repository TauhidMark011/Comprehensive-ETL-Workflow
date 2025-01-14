#Contains functions to load the transformed data into a CSV file.
import pandas as pd
from utils import log

def load_data(data, output_file="transformed_data.csv"): #to save the final output.
    # This function saves the transformed data to a CSV file (default: "transformed_data.csv")
    log(f"Saving transformed data to {output_file}")
    #Loads data into the target destination (CSV or database).
    data.to_csv(output_file, index=False) # Using pandas to save the DataFrame to a CSV file
    log("Data loading completed..!")
    # Logging the completion of the loading process