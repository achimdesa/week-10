# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA

def load_and_preprocess_data(data_path):
    """Load and preprocess the dataset."""
    # Load the dataset
    df = pd.read_csv(data_path)
    
    # Convert Date column to datetime format with automatic inference
    df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True)
    
    # Drop missing values, if any
    df.dropna(inplace=True)
    
    # Display the first few rows and data info
    print("First few rows of data:")
    print(df.head())
    print("\nData Info After Preprocessing:")
    df.info()
    
    return df

def plot_price_trend(df):
    """Plot the price trend over time."""
    plt.figure(figsize=(14, 7))
    sns.lineplot(data=df, x='Date', y='Price')
    plt.title('Brent Oil Prices Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price (USD per Barrel)')
    plt.show()

def fit_arima_model(df, order=(5, 1, 0)):
    """Fit an ARIMA model to the Brent oil price data."""
    model = ARIMA(df['Price'], order=order)  # Order (p,d,q) needs tuning
    model_fit = model.fit()
    print(model_fit.summary())
    return model_fit

def plot_residuals(model_fit):
    """Plot residuals to understand the model's performance."""
    residuals = model_fit.resid
    plt.figure(figsize=(10, 6))
    sns.histplot(residuals, kde=True)
    plt.title('Residuals of ARIMA Model')
    plt.xlabel("Residuals")
    plt.show()

