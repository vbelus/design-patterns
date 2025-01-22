from base_pipeline import DataProcessingPipeline

class FilterPipeline(DataProcessingPipeline):
    """Pipeline that filters out specific data."""
    
    def process_data(self, data):
        print("Processing data: filtering out 'raw_data_2'.")
        return [item for item in data if item != "raw_data_2"]
