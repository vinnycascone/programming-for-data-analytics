
# programming-for-data-analytics

# Wind Speed Analysis Project

## Overview


This project, made by Vincenzo Cascone for the Programming for Data Analytics module, focuses on analyzing wind speed data using Python. The code has been executed leveraging Jupyter Notebooks and powerful Python libraries and the goal of it is to process, visualize, and derive insights from the dataset downloaded about the windspeed across the country. 

The project has been made also for forecasting wind speed, evaluating patterns over time, and assessing potential for renewable energy projects like wind farms.  



## Structure and actions of the code


- **Data Preprocessing:** Cleaned and structured raw wind speed data.  
- **Exploratory Data Analysis (EDA):** Visualized wind speed trends, distributions, and seasonal patterns.  
- **Statistical Analysis:** Identified key metrics like mean, variance, and outliers in wind speed data.  
- **Time Series Analysis:** Investigated temporal patterns to understand how wind speed evolves over time.  
- **Predictive Modeling:** Explored machine learning techniques for wind speed prediction.  



## Tools and Libraries


This project utilizes the following tools and libraries:  
- **Jupyter Notebook:** For running Python code.  
- **main Python Libraries for references:**  
  - [Pandas](https://pandas.pydata.org/) for data manipulation.  
  - [NumPy](https://numpy.org/doc/) for numerical computations.  
  - [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/) for data visualization.  
  - [Statsmodels](https://www.statsmodels.org/) for time series analysis.  
  - [Scikit-learn](https://scikit-learn.org/) for machine learning models



## Data Source


The datasets used for this project contains wind speed measurements over a specific time period:
- [MTM04 - Wind, Maximum Gale Gust (>33.5 Knots)](https://data.gov.ie/dataset/mtm04-wind-maximum-gale-gust-335-knots/resource/855de0b5-1e1b-4291-a3f7-0f706b0c44a7)
- [Dublin Airport Monthly Data](https://data.gov.ie/dataset/dublin-airport-monthly-data/resource/f43c57e5-5bab-4dc2-9318-24c31525878a)



## Structure


- **`windspeed.ipynb`**: The main Jupyter Notebook containing all code, analysis, and visualizations. 
- **README.md** with the extended library and study references 
- **Data Folders:** Includes the raw dataset files used for the analysis:
  - **MTM04** main analyzed dataset [MTM04 - Wind, Maximum Gale Gust (>33.5 Knots)](https://data.gov.ie/dataset/mtm04-wind-maximum-gale-gust-335-knots/resource/855de0b5-1e1b-4291-a3f7-0f706b0c44a7)
  - **cleaned_wind_data** cleaned version of main dataset
  - **mly532** dataset used to analyze wind correlation with weather and rainfall
  

-------


# **Study References: Data Loading and Preprocessing in Python**

## Data Acquisition and cleaning: 

## **Weather Library**
- [MTM04 - Wind, Maximum Gale Gust (>33.5 Knots)](https://data.gov.ie/dataset/mtm04-wind-maximum-gale-gust-335-knots/resource/855de0b5-1e1b-4291-a3f7-0f706b0c44a7)

## **Working with CSV Files**

- [pandas `read_csv` Documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
- [pandas `to_csv` Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)

---

## **Inspecting Datasets**

- [pandas `DataFrame.info` Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html)
- [pandas `DataFrame.describe` Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)
- General guide on [Exploratory Data Analysis (EDA)](https://www.analyticsvidhya.com/blog/2021/06/exploratory-data-analysis-eda-a-step-by-step-guide/)

---

## **Handling Missing Data**

- [pandas `dropna` Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html)
- [pandas `fillna` Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html)
- Article: [Dealing with Missing Data in Python](https://towardsdatascience.com/how-to-handle-missing-data-8646b18db0d4)

---

## **Working with Dates**

- [pandas `to_datetime` Documentation](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html)
- Article: [Working with Dates in Python Using pandas](https://realpython.com/python-datetime/)

---

## **Saving and Organizing Data**

- [pandas `DataFrame.to_csv` Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)

---

## **Python File Handling**

- [Python `os` Module Documentation](https://docs.python.org/3/library/os.html)
- Article: [File Handling in Python](https://www.geeksforgeeks.org/file-handling-python/)

---

# **Exploratory Data Analysis**

**DataCamp: Time Series Plotting with Matplotlib**   
[Basics of time series plotting using Matplotlib](https://www.datacamp.com/community/tutorials/time-series-python)  

**DelftStack: Seaborn Line Plots for Time Series**    
[Seaborn's `lineplot` to visualize time series data](https://www.delftstack.com/howto/python/seaborn-time-series-plot/)  


## **Data Visualization**

### **Data Visualization with Python**
- [Data Visualization with Python - GeeksforGeeks](https://www.geeksforgeeks.org/data-visualization-with-python/): 

### Matplotlib  
- [Matplotlib Documentation](https://matplotlib.org/)  
   

### Seaborn  
- [Seaborn Documentation](https://seaborn.pydata.org/)  
    


# Wind Speed Analysis and Data Science


## Python Data Science and Libraries
-⁠  ⁠[Pandas Documentation](https://pandas.pydata.org/)  

-⁠  [NumPy Documentation](https://numpy.org/doc/)

-⁠  ⁠[Matplotlib Documentation](https://matplotlib.org/stable/contents.html)

-⁠  ⁠[Seaborn Documentation](https://seaborn.pydata.org/)

---

## Time Series Analysis

-⁠  ⁠[Scikit-learn Documentation](https://scikit-learn.org/)

### ARIMA Time Series Forecasting  
- [Time Series Forecasting Tutorial](https://www.datacamp.com/tutorial/tutorial-time-series-forecasting)    

### Time Series in Python (Pandas)  
- [Working with Time Series in Python](https://www.timescale.com/blog/how-to-work-with-time-series-in-python/)  

---

## Machine Learning and Wind Speed Prediction

- [Statsmodels](https://www.statsmodels.org/) 

### Linear Regression using Scikit-Learn  
- [Scikit-Learn Documentation](https://scikit-learn.org/)  

### Train-Test Split and Model Evaluation  
- [Understanding Train Test Split](https://builtin.com/data-science/train-test-split)    

---

## **Data Handling and Pandas**  

### Pandas Documentation  
- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/reshaping.html)  
  Learn how to manipulate and analyze data with Pandas.  

### Pivot Tables in Pandas  
- [Pandas Pivot Table in Python](https://www.machinelearningplus.com/pandas/pandas-pivot-table-in-python/)  
  Guidance on creating pivot tables for data summarization.  

---

## **Wind Power Calculation**  

### Wind Power Equation and Rotor Area  
- [Wind Energy and Power Calculations](https://www.e-education.psu.edu/emsc297/node/649)   

---

## **API Data Fetching**  

### Meteomatics API  
- [Meteomatics Weather API](https://www.meteomatics.com/en/api/getting-started/)  

---

## **Correlation Analysis and Statistics**  

### Correlation Matrix and Heatmaps  
- [How to Create a Seaborn Correlation Heatmap in Python](https://medium.com/@szabo.bibor/how-to-create-a-seaborn-correlation-heatmap-in-python-834c0686b88e)  
  Example of how to create heatmaps for visualizing correlations in data.  

### Pearson Correlation  
- [Pearson Correlation Coefficient Guide & Examples](https://www.scribbr.com/statistics/pearson-correlation-coefficient/)  


---

