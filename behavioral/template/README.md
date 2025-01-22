# Data Processing with the Template Method Design Pattern

This directory demonstrates the **Template Method Design Pattern** in Python, using a data processing pipeline example. The Template Method Pattern allows us to define the structure of an algorithm in a base class, while letting subclasses customize specific steps.

---

## **Why Use the Template Method Design Pattern?**

### Let's use an analogy : baking cookies 🍪
- The **recipe** (base class) tells you the order: mix ingredients, bake, and decorate.
- You can **customize** some steps: maybe you want chocolate chips or sprinkles (subclass methods).
- But you don’t need to rewrite the recipe for every new flavor—just tweak the parts you want to change!

This design pattern is perfect when:
1. You want to **reuse common steps** across different implementations.
2. You need **consistent structure** but with room for customization.

In short: **It saves you time and effort by avoiding code duplication while keeping everything organized and flexible.**

---

## **Example Scenario: Data Processing Pipelines**

This example focuses on building a data processing pipeline with the following structure:
1. **Read Data**: Get raw data from a source.
2. **Process Data**: Transform the data in some way (customizable).
3. **Write Data**: Save the processed data to a destination.

The base class implements the shared steps (reading and writing data) and enforces the pipeline structure, while subclasses handle the data processing logic.

---

## **Directory Structure**

- **`base_pipeline.py`**: 
  Defines the `DataProcessingPipeline` abstract base class, which outlines the pipeline structure (`run` method) and includes default implementations for reading and writing data.
  
- **`uppercase_pipeline.py`**: 
  A concrete pipeline that converts all data to uppercase.

- **`filter_pipeline.py`**: 
  A concrete pipeline that filters out specific data items.

- **`alternate_source_pipeline.py`**: 
  A concrete pipeline that reads data from an alternate source and makes no changes to the data.

- **`example.py`**: 
  Demonstrates how to use the different pipelines to process data.

---

## **How It Works**

### 1. Base Class (`DataProcessingPipeline`)
The base class provides:
- A `run` method that defines the pipeline structure.
- Default implementations for:
  - **`read_data`**: Simulates reading data from a source.
  - **`write_data`**: Simulates writing data to a destination.
- An abstract **`process_data`** method that subclasses must implement.

### 2. Subclasses
Subclasses customize the `process_data` step to implement specific logic:
- **`UppercasePipeline`**: Converts all data to uppercase.
- **`FilterPipeline`**: Filters out unwanted items.
- **`AlternateSourcePipeline`**: Reads data from a different source and makes no changes.