from abc import ABC, abstractmethod

class DataProcessingPipeline(ABC):
    """Abstract base class for a data processing pipeline."""
    
    def run(self):
        """Template method defining the pipeline structure."""
        data = self.read_data()
        processed_data = self.process_data(data)
        self.write_data(processed_data)
    
    def read_data(self):
        """Default implementation for reading data (e.g., from a file)."""
        print("Reading data from source...")
        return ["raw_data_1", "raw_data_2", "raw_data_3"]
    
    @abstractmethod
    def process_data(self, data):
        """Abstract method for processing data. Subclasses must implement this."""
        pass
    
    def write_data(self, data):
        """Default implementation for writing data (e.g., to a file)."""
        print("Writing processed data to destination...")
        for item in data:
            print(f"  - {item}")
