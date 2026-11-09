# Gold Price Predictor

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Framework](https://img.shields.io/badge/scikit--learn-latest-orange.svg)
![App](https://img.shields.io/badge/streamlit-deployed-red.svg)

[Access the Live Application](https://8xrxkoq3hbsddj95wk84tk.streamlit.app/)

This project utilizes a `RandomForestRegressor` model to predict historical gold prices (in USD) based on temporal data. It includes a complete end-to-end pipeline from data preprocessing to a user-friendly Streamlit web application for real-time predictions.

## Features
- Data preprocessing of historical gold price data.
- Machine learning model (RandomForestRegressor) trained on historical data.
- Streamlit web application for interactive predictions.

## Prerequisites
- Python 3.x
- pip

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bruzz-bruzz/gold-price-predictor
   cd gold-price-predictor
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Training the Model
To train the model and generate the `predictor.pkl` file:
```bash
python main.py
```

### Running the Web Application
To run the Streamlit app:
```bash
streamlit run streamlit_app.py
```

## Model Evaluation
The following performance metrics were obtained from the model:

| Metric | Value |
| :--- | :--- |
| Mean Absolute Error (MAE) | 10.631372225414218 |
| Mean Absolute Percentage Error (MAPE) | 0.01604538497626848 |
| R-squared (R2) | 0.9990064389033357 |
| Mean Squared Error (MSE) | 263.4236936826387 |
| Root Mean Squared Error (RMSE) | 16.230332519164193 |

## Data Source
The dataset used for training is from Kaggle:
[Kaggle Dataset](https://www.kaggle.com/datasets/rizkykiky/gold-price-dataset)

## Project Structure
- `data.csv`: Historical gold price data.
- `main.py`: Script to preprocess data and train the `RandomForestRegressor` model.
- `predictor.pkl`: Serialized trained model.
- `streamlit_app.py`: Streamlit web interface for making predictions.
- `requirements.txt`: Project dependencies.
- `.github/workflows/wake.yml`: CI/CD configuration.
