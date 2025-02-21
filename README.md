# Brent Oil Prices Analysis and Dashboard Development

## Task 1: Time Series Analysis and Basic EDA

### Overview
The goal of this analysis is to examine historical Brent oil prices, detect significant changes, and provide insights on how political and economic events affect price fluctuations. Using data from May 20, 1987, to September 30, 2022, we explore statistical patterns in Brent oil prices. This analysis enables stakeholders such as policymakers, investors, and energy companies to make data-driven decisions in a volatile market.

### Data Analysis Workflow
Steps Overview:
1.	Data Loading & Preprocessing
We began by loading the dataset (BrentOilPrices.csv). Data preprocessing included:
o	Converting dates into a consistent datetime format.
o	Handling any missing values.
Dataset Summary:
o	Total Records: 9,011
o	Columns: Date (datetime), Price (float)
o	Memory Usage: 140.9 KB
2.	Exploratory Data Analysis (EDA)
A time series line plot of Brent oil prices from 1987 to 2022 was generated, revealing long-term trends and fluctuations. Observations show notable periods of both stability and volatility, likely influenced by global events, economic sanctions, and political policies in oil-producing countries.
3.	Model Selection
For modeling and analyzing trends, we selected the ARIMA (Auto-Regressive Integrated Moving Average) model, specifically ARIMA(5,1,0). ARIMA provides a framework for analyzing time-dependent structures, capturing both autoregressive (AR) and moving average (MA) components while accounting for integration (differencing).
4.	Change Point Detection & Model Diagnostics
Our ARIMA model output includes key performance metrics and diagnostics, offering insights into the price changes over time and identifying patterns in residuals that may indicate significant market shifts.
5.	Interpretation & Insights
Results from the ARIMA model highlight how past values influence current price trends. This step involves interpreting model diagnostics to provide actionable insights for stakeholders.

### Assumptions and Limitations
•	Assumptions:
o	The data represents accurate historical prices for Brent oil.
o	No external economic factors, aside from price, are included in the model.
•	Limitations:
o	Forecasting may be impacted by unpredictable external events (e.g., sudden geopolitical conflicts).
o	Seasonal or periodic factors may not be fully captured by the ARIMA model alone.
### Key Observations and Next Steps
•	Residual Analysis: The ARIMA model’s residuals indicate a potential for improvement. High kurtosis suggests that price changes may have significant peaks and volatility, highlighting opportunities for further model tuning (e.g., switching to a GARCH model to account for volatility clustering).
•	Further Model Enhancements: Future analyses will consider change point detection techniques, such as Bayesian change point models, to identify sudden shifts more accurately.
•	Insights for Stakeholders: Observing volatility patterns can guide investment strategies, policy planning, and risk management.
