# Urban PM2.5 Concentration Analysis

A comprehensive analysis of annual mean PM2.5 concentrations in urban areas worldwide. This project focuses on data retrieval, cleaning, exploratory analysis, and interactive reporting to assess environmental health risks.


## Table of Contents
- [Project Overview]
- [Usage]
- [Project Structure]
- [Key Features]
- [Streamlit Dashboard]
- [Testing]
- [Acknowledgments]

---

## Project Overview
This project analyzes population-weighted PM2.5 concentrations in urban areas using real-world data from the World Health Organization (WHO). The workflow includes:

1. **Data Retrieval**: Load CSV/JSON data from local/remote sources
2. **Data Cleaning**: Handle missing values and detect outliers using statistical methods
3. **Exploratory Analysis**: Perform residual analysis and visualize trends
4. **Reporting**: Build an interactive dashboard for policy/ML readiness

**Key Technologies**:  
Python, Pandas, NumPy, Matplotlib, Seaborn, Streamlit

---

## Usage

### Jupyter Notebooks
Run notebooks in sequence for full analysis:
```bash
jupyter lab
```
1. **`01_data_loading_exploration.ipynb`**  
   - Initial data profiling
   - Basic statistical summaries
   - Data type validation

2. **`02_cleaning_missing_outliers.ipynb`**  
   - Missing value imputation
   - Outlier detection (IQR/Z-score)
   - Data validation checks

3. **`03_data_summary_and_features.ipynb`**
   - summary statistics
   - Residual analysis for regression

### Streamlit Dashboard
Launch the interactive report:
```bash
streamlit run streamlit_app/Home.py
```

---

## Project Structure
```
urban-pm25-analysis/
├── data/               # Raw → Cleaned data pipeline
├── notebooks/          # Step-by-step analysis
├── scripts/            # Reusable Python modules
├── streamlit_app/      # Interactive dashboard
└── tests/              # Data cleaning unit tests
```

---

## Key Features

### Data Processing
- **Missing Value Handling**: Forward-fill, interpolation, and flagging
- **Outlier Detection**: IQR ranges, Z-score thresholds, visual diagnostics
- **Anomaly Detection**: Residual analysis from regression models

### Visualization
- Interactive choropleth maps of PM2.5 distribution
- Boxplots for country-wise comparisons
- Time-series analysis of pollution trends

### Reproducibility
- Modular code (Jupyter + Python scripts)
- Config-driven file paths
- Unit-tested data cleaning logic

---

## Streamlit Dashboard
Navigate through 4 interactive pages:

| Page | Description |
|------|-------------|
| **Home** | Project introduction and methodology |
| **Urban PM2.5 Overview** | Geographic trends and country comparisons |
| **Data Quality Report** | Missing values and outlier analysis |
| **Regression Analysis** | Residual plots and anomaly detection |


---

## Testing
Validate data cleaning functions:
```bash
pytest tests/test_cleaning.py -v
```
Tests include:
- Missing value imputation logic
- Outlier detection thresholds
- Data type consistency checks

---

## Acknowledgments
- World Health Organization (WHO) for the dataset
- Streamlit community for dashboard components
- Pandas/NumPy for data processing tools
```
