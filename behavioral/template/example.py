from uppercase_pipeline import UppercasePipeline
from filter_pipeline import FilterPipeline
from alternate_source_pipeline import AlternateSourcePipeline

def main():
    # Run the Uppercase Pipeline
    print("Running Uppercase Pipeline:")
    uppercase_pipeline = UppercasePipeline()
    uppercase_pipeline.run()
    
    print("\n" + "="*40 + "\n")
    
    # Run the Filter Pipeline
    print("Running Filter Pipeline:")
    filter_pipeline = FilterPipeline()
    filter_pipeline.run()

    # Run the Alternate Source Pipeline
    print("Running Alternate Source Pipeline:")
    filter_pipeline = AlternateSourcePipeline()
    filter_pipeline.run()

if __name__ == "__main__":
    main()
