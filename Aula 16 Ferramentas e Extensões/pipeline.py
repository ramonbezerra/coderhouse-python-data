import pandas as pd
import yfinance as yf

def get_finance_data_name(symbol):
    try:
        return yf.Ticker(symbol).info['shortName']
    except:
        return f''
    
def get_dividends_by_period(period, symbol):
    try: 
        return yf.Ticker(symbol).history(period=period).Dividends.sum() # 1d, 1w, 1m, 3m, 6m, 5y, 10y, ytd, max
    except:
        return 0

df = pd.read_csv('listing_status.csv', header=0)

df['ipoDate'] = pd.to_datetime(df['ipoDate'], format='%Y-%m-%d')
df['delistingDate'] = pd.to_datetime(df['delistingDate'], format='%Y-%m-%d')
df['assetType'] = df['assetType'].astype('category')
df['exchange'] = df['exchange'].astype('category')

df['name'] = df.apply(lambda x: get_finance_data_name(x.symbol) if pd.isna(x['name']) or x['name'] == '' else x.name, axis=1)

df.dropna(subset=['name', 'symbol'], inplace=True)
df.drop(df[df.name == ''].index, inplace=True)

df.drop(df[df.exchange == 'NYSE ARCA'].index, inplace=True)
df.drop(df[df.exchange == 'NYSE MKT'].index, inplace=True)
df.drop(df[df.exchange == 'BATS'].index, inplace=True)

rate_exchange = df.exchange.value_counts(normalize=True)
rate_asset = df.assetType.value_counts(normalize=True)

exchange_sample = df.groupby('exchange').apply(lambda x: x.sample(int(10 * rate_exchange[x.name]))).droplevel('exchange')
exchange_sample['dividends_last_5_years'] = exchange_sample.apply(lambda x: get_dividends_by_period('5y', x.symbol), axis=1)
exchange_sample.to_csv('exchange_sample.csv', index=False)

asset_sample = df.groupby('assetType').apply(lambda x: x.sample(int(10 * rate_asset[x.name]))).droplevel('assetType')
asset_sample['dividends_last_5_years'] = asset_sample.apply(lambda x: get_dividends_by_period('5y', x.symbol), axis=1)
asset_sample.to_csv('asset_sample.csv', index=False)