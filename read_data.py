import pandas as pd

def read_data(link):
    #URL of the raw CSV file in Github and return in df
    csv_url = link
    df = pd.read_csv(csv_url)
    return df


