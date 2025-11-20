import pandas as pd
import logging
import os

class DataIngestion:
    def __init__(self, file_path):
        self.file_path = file_path

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion started")
        df = pd.read_csv(self.file_path)
        logging.info(f"Data shape: {df.shape}")
        return df

