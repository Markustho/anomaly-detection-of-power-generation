# main.py

# 1. Imports
import os
import sys
import logging
from dataloader import load_all_data



# 4. Main Function
def main():
    """Main entry point of the program."""
    
    #Load the data
    #create the new dataframe for output data
    #create plots

    # Input Data (could be from command line, a file, etc.)
    input_data = "Hello, world!"

    # Process data
    result = process_data(input_data)

    # Output result
    logging.info(f"Result: {result}")


if __name__ == "__main__":
    # Define the file paths for 2017 and 2016
    file_paths = {
        'data_2017': "../../data/raw/Onsite-MetMast-SCADA-data-2017.xlsx",
        'scada_2017': "../../data/raw/Wind-Turbine-SCADA-signals-2017_0.xlsx",
        'failures_2017': "../../data/raw/opendata-wind-failures-2017.xlsx",
        'data_2016': "../../data/raw/Onsite-MetMast-SCADA-data-2016.xlsx",
        'scada_2016': "../../data/raw/Wind-Turbine-SCADA-signals-2016.xlsx",
        'failures_2016': "../../data/raw/Historical-Failure-Logbook-2016.xlsx"
    }

    # Load all Excel files into a dictionary of DataFrames
    data_frames = load_all_data(file_paths)
    main()