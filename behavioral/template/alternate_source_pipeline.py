from base_pipeline import DataProcessingPipeline

class AlternateSourcePipeline(DataProcessingPipeline):
    """Pipeline that reads data from an alternate source and leaves it unmodified."""
    
    def read_data(self):
        """Simulate reading data from a different file source."""
        print("Reading data from an alternate source...")
        return ["alt_data_1", "alt_data_2", "alt_data_3"]
    
    def process_data(self, data):
        """No-op: The data is not modified."""
        print("Processing data: no changes made.")
        return data
