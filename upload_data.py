import pandas as pd

def read_data(csv_url):
    #URL of the raw CSV file in Github and return in df
    df = pd.read_csv(csv_url)
    return df


