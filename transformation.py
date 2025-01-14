# Contains functions for transforming data, such as unit conversions and cleaning.
from utils import log # Importing log function to track transformation progress

def transform_data(input_data):
    #Performs data transformations, such as converting units (e.g., height and weight)
    log("Starting data transformation")
    #Convert height from inches to meters(To convert inches to meters, you should multiply your length value by 0.0254)
    input_data["height"] = input_data["height"] * 0.0254
    # Convert weight from pounds to kilograms (1 pound = 0.453592 kilograms)
    input_data["weight"] = input_data["weight"] * 0.453592
    log("Data transformation completed")
    return input_data  # Returning the transformed data
