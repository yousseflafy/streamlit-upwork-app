## Title: Urban PM2.5 Air Pollution: A Global Exploratory Data Analysis


#### **Meta Data**

Indicator name:
Annual mean concentration of particulate matter of less than 2.5 microns of diameter (PM2.5) [ug/m3] in urban areas
Short name:
Annual mean PM2.5 concentration in urban areas
Data type:
Statistic
Indicator Id:
4674
Topic:
Risk factors
ISO Health Indicators Framework
Environmental factors
Rationale:
Air pollution consists of many pollutants, among other particulate matter. These particles are able to penetrate deeply into the respiratory tract and therefore constitute a risk for health by increasing mortality from respiratory infections and diseases, lung cancer, and selected cardiovascular diseases.
Definition:
The mean annual concentration of fine suspended particles of less than 2.5 microns in diameters is a common measure of air pollution. The mean is a population-weighted average for urban population in a country.
Method of measurement
Concentration of PM2.5 are regularly measured from fixed-site,  population-oriented monitors located within the metropolitan areas. High-quality measurements of PM concentration from all the monitors in the metropolitan area can be averaged to develop a single estimate.  
Method of estimation:
Although PM is measured at many thousands of locations throughout the world, the amount of monitors in different geographical areas vary, with some areas having little or no monitoring. In order to produce global estimates at high resolution (0.1◦ grid‐cells), additional data is required. Annual urban mean concentration of PM2.5 is estimated with improved modelling using data integration from satellite remote sensing, population estimates, topography and ground measurements.
Preferred data sources:
Special studies
Expected frequency of data dissemination:
Every 2-3 years
Expected frequency of data collection:
Every 2-3 years



### **Data Sources**
* https://www.who.int/data/gho/data/themes/air-pollution/who-air-quality-database/2022






### **Project Overview**  
This project focuses on retrieving, cleaning, and exploring real-world data on **annual mean PM2.5 concentrations** in urban areas across different countries. The dataset provides a population-weighted average of fine particulate matter (PM2.5) in cities, which is a critical indicator of environmental health risk.

You will simulate an end-to-end exploratory data analysis (EDA) process, aligning with the following objectives:
- Retrieve and load the data from CSV, JSON, and/or remote sources.
- Clean the data by managing missing values and identifying outliers using statistical techniques.
- Use residual-based methods to flag anomalies.
- Document your process in Jupyter Notebooks and build an interactive Streamlit dashboard for reporting findings.

This project mirrors a professional workflow you'd follow in data science consulting or research to prepare high-quality environmental data for downstream ML tasks or policy analysis.





### **Folder Structure**

```
urban-pm25-analysis/
│
├── data/
│   ├── raw/                                # Unprocessed original files
│   │   └── WHO_PM25_urban_2022.csv
│   ├── interim/                            # Partially cleaned, exploratory data
│   │   └── pm25_with_missing_flags.csv
│   └── processed/                          # Final cleaned dataset
│       └── pm25_cleaned.csv
│
├── notebooks/
│   ├── 01_data_loading_exploration.ipynb   # CSV/JSON/API loading, initial profiling
│   ├── 02_cleaning_missing_outliers.ipynb  # Outlier detection, imputation
│   └── 03_data_summary_and_features.ipynb  # Data transformation, final prep
│
├── scripts/
│   ├── data_loader.py                      # Functions to load local/remote data
│   ├── cleaning.py                         # Handling nulls, outliers, and residuals
│   ├── preprocessing.py                    # Reshaping, scaling, and encoding
│   └── config.py                           # Filepaths and global vars
│
├── streamlit_app/                          # Streamlit report dashboard
│   ├── Home.py                             # Dashboard homepage
│   ├── pages/
│   │   ├── 1_Urban_PM25_Overview.py        # Country-wise trends, maps
│   │   ├── 2_Missing_Outlier_Report.py     # Residuals, missing value analysis, data cleaning
│   │   └──3_regression_analysis
|   |
│   
├── tests/
│      └── test_cleaning.py                    # Unit tests for your cleaning module
|
├── requirements.txt                        # All Python dependencies
├── README.md                               # Project overview, how to run, and usage
└── .gitignore
```







