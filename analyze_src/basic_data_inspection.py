from abc import ABC, abstractmethod 

import pandas as pd 

# Abstract base class for Data Inspection Stragedies 
# --------------------------------------------------
# This class defines a common interface for data inspection stragedies 
# Subclasses must implement the inspection method. 
class DataInspectionStragedy(ABC):
    @abstractmethod
    def Inspect(self, df: pd.DataFrame): 
        """
        Perform a specific type of data inspection 

        Parameters:
        df (pd.DataFrame): The dataframe on which the inspection

        Returns:
        None. This method prints the inspection results directly 
        """
        pass

# Concrete Stragedy for Data Types inspection 
# -------------------------------------------
# This Stragedy Inspects the data types of each column and count 
class DataTypesInspectionStragedy(DataInspectionStragedy):
    def Inspect(self, df: od.DataFrame):

        """
        """
        print()