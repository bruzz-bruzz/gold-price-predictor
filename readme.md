# Gold Price Predictor

[Link](https://8xrxkoq3hbsddj95wk84tk.streamlit.app/)

A machine learning project to predict the price of gold (in USD) based on the date.

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

## Data Source
The dataset used for training is from Kaggle:
https://www.kaggle.com/datasets/rizkykiky/gold-price-dataset

## Project Structure
- `data.csv`: Historical gold price data.
- `main.py`: Script to preprocess data and train the `RandomForestRegressor` model.
- `predictor.pkl`: Serialized trained model.
- `streamlit_app.py`: Streamlit web interface for making predictions.
- `requirements.txt`: Project dependencies.
- `.github/workflows/wake.yml`: CI/CD configuration.
