from base_pipeline import DataProcessingPipeline

class UppercasePipeline(DataProcessingPipeline):
    """Pipeline that converts data to uppercase."""
    
    def process_data(self, data):
        print("Processing data: converting to uppercase.")
        return [item.upper() for item in data]
