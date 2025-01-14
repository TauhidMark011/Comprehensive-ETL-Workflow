# Main script to run the ETL process, This will orchestrate the entire ETL process by calling functions from the other files.
from extraction import extract_data #Importing the function to extract data from different file formats
from transformation import transform_data #Importing the function to perform transformations on the extracted data
from loading import load_data  # Importing the function to load the transformed data into the desired format
from utils import log # Importing the log function to track the progress of the ETL process

if __name__ == "__main__": # This block will execute only if this script is run directly
    log("ETL process started")
    # Extract: Call the function to extract data from CSV, JSON, and XML files
    extracted_data = extract_data()
    print(type(extracted_data))  # Debugging: Checking the type of extracted data
    print(extracted_data.head())  # Debugging: Checking the first few rows of extracted data
    #Transform: Call the transformation function to modify the extracted data
    transformed_data = transform_data(extracted_data)
    #Load: Call the function to save the transformed data to a CSV file
    load_data(transformed_data)
    log("ETL process completed")
