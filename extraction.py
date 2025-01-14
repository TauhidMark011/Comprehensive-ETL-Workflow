# Contains all data extraction functions, Contains functions to extract data from CSV, JSON, and XML files.
# Importing required libraries
import pandas as pd  # Importing pandas for data manipulation
import json  # Importing json to parse JSON files
import xml.etree.ElementTree as ET # Importing XML parser to work with XML files
import glob  # Importing glob to handle file path patterns
from utils import log # Importing log function for logging extraction progress

# Set the source directory where the data files are located
source_dir = r"D:\source"
# Function to extract CSV files
def extract_csv(file_path):
    log(f"Extracting data from {file_path}")
    return pd.read_csv(file_path) # Using pandas to read CSV files into a DataFrame
# Function to extract JSON files
def extract_json(file_path):
    log("Extracting data from {file_path}") # Logging the extraction process
    with open(file_path, "r") as json_file:
        data = [json.loads(line) for line in json_file] # Reading each line of the JSON file
    return pd.DataFrame(data) # Returning data as a pandas DataFrame
#Function to extract XML Files
def extract_xml(file_path):
    log(f"extracting data from {file_path}")
    tree = ET.parse(file_path) # Parsing the XML file
    root = tree.getroot()  # Getting the root element of the XML
    data = []  # Empty list to hold parsed data
    for person in root.findall("person"): # Loop through XML elements and extract relevant data

        data.append({
            "name": person.find("name").text, # Extract name
            "height" : float(person.find("height").text), # Extract and convert height to float
            "weight" : float(person.find("weight").text) # Extract and convert weight to float
        })
    return pd.DataFrame(data) # Returning data as a pandas DataFrame

#Master function to extract all data 
def extract_data():
    # Extracts data from various all CSV, JSON, and XML files in the source directory. Returns: pandas.DataFrame
    all_data = pd.DataFrame()  # Initialize an empty DataFrame to hold all the extracted data
    #Extract all csv files
    for file_path in glob.glob(f"{source_dir}/*.csv"):
        all_data = pd.concat([all_data, extract_csv(file_path)],ignore_index=True)
    #Extract all Json files
    for file_path in glob.glob(f"{source_dir}/*.json"):
        all_data = pd.concat([all_data, extract_json(file_path)],ignore_index=True)
    #Extraxct all Xml files
    for file_path in glob.glob(f"{source_dir}/*.xml"):
        all_data = pd.concat([all_data, extract_xml(file_path)],ignore_index=True)
    log("Data extraction completed")
    return all_data
# Returning the combined DataFrame with data from all file types