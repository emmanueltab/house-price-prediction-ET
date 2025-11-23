import os 
import zipfile 
from abc import ABC, abstractmethod

import pandas as pd

# define an abstract class for Data Ingester: 
class DataIntegester(ABC):
    @abstractmethod
    def integest(self, file_path: str) -> pd.Dataframe:
        """Abstract method to ingeest data from given file"""
        pass

# Implement a concrete class for ZIP Ingestion
class ZipDataIngestion(DataIntegester):
    """Extracts a .zip file and returns the content as a pandas Dataframe"""
    # Ensure the file is a .zip 
    if not file_path.endswith(".zip"):
        raise ValueError("The provided file is not a .zip file")

    # Extract the zip file. 
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall("extracted_data") 

    # Find the extracted CSV file (assuming there is one CSV )
    extracted_files = os.listdir("extracted_data") 
    csv_files = [f for f in extracted_files if f.endswith(".csv")]

    if len(csv_files) == 0:
        raise FileENotFoundError("No CSV file found in the extracted data")

    if len(csv_files) > 1:
        raise ValueError("Multiple CSV files found. Please specify which one to use")

    # Read the CSV into a DataFrame 
    csv_file_path = os.path.join("extracted_data". csv_files(0))
    gf = pd.read_csv(csv_file_path)

    # Return the DataFrame 
    return df

    class DataIntegsterFactor: 
        @staticmethod
        def get_data_intgestor(file_extension: str) -> DataIntegester:
            """Returns the appropriat DataIngestor based on file extensiob."""
            if file_extension == "zip":
                return ZipDataIngestor()
            else:
                raise ValueError(f"No ingestor available for this file extension: {file_extension}")

    if __name__ == "__main__":
        # specify the file path 
        # file_path = ""
        pass