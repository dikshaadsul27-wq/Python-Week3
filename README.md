# Python-Week3
# Sales Data Analysis

This project provides a simple exploratory analysis of sales data using **Python** and **Pandas**.  
It demonstrates how to load a dataset, inspect its structure, handle missing values, and compute key business insights such as total revenue and top-performing products.

## Features
- Load and preview sales data from a CSV file
- Display dataset shape, data types, and missing values
- Handle missing values:
  - Fill with column averages
  - Optionally drop rows with missing values
- Calculate column-wise averages, maximums, and minimums
- Compute total revenue
- Rank products by revenue
- Identify the best-selling product

## Requirements
- Python 3.x
- Pandas library

Install dependencies with:
```bash
pip install pandas

## Usage
- Place your sales dataset in the project directory as sales_data.csv.
- Run the script:
python sales_analysis.py


The script will output:
- Dataset overview
- Missing value summary
- Key statistics (averages, max, min)
- Total revenue
- Products ranked by revenue
- Best product by sales
