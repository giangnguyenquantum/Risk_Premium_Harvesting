import pandas as pd

def get_TWAP_price(historical_price_total_df):
    TWAP_df=pd.DataFrame()
    TWAP_df['OC_dist']=abs(historical_price_total_df['Open']-historical_price_total_df['Close'])
    TWAP_df['OH_dist']=historical_price_total_df['High']-historical_price_total_df['Open']
    TWAP_df['OL_dist']=historical_price_total_df['Open']-historical_price_total_df['Low']
    TWAP_df['HL_dist']=historical_price_total_df['High']-historical_price_total_df['Low']
    TWAP_df['LC_dist']=historical_price_total_df['Close']-historical_price_total_df['Low']
    TWAP_df['HC_dist']=historical_price_total_df['High']-historical_price_total_df['Close']
    TWAP_df['OHLC_dist']=TWAP_df['OH_dist']+TWAP_df['HL_dist']+TWAP_df['LC_dist']
    TWAP_df['OLHC_dist']=TWAP_df['OL_dist']+TWAP_df['HL_dist']+TWAP_df['HC_dist']
    TWAP_df['OH_mean']=0.5*(historical_price_total_df['High']+historical_price_total_df['Open'])
    TWAP_df['OL_mean']=0.5*(historical_price_total_df['Low']+historical_price_total_df['Open'])
    TWAP_df['HL_mean']=0.5*(historical_price_total_df['High']+historical_price_total_df['Low'])
    TWAP_df['LC_mean']=0.5*(historical_price_total_df['Low']+historical_price_total_df['Close'])
    TWAP_df['HC_mean']=0.5*(historical_price_total_df['High']+historical_price_total_df['Close'])
    TWAP_df['OHLC_twap']=(TWAP_df['OH_dist']*TWAP_df['OH_mean']+\
        TWAP_df['HL_dist']*TWAP_df['HL_mean']+TWAP_df['LC_dist']*TWAP_df['LC_mean'])\
        /TWAP_df['OHLC_dist']
    TWAP_df['OLHC_twap']=(TWAP_df['OL_dist']*TWAP_df['OL_mean']+\
        TWAP_df['HL_dist']*TWAP_df['HL_mean']+TWAP_df['HC_dist']*TWAP_df['HC_mean'])\
        /TWAP_df['OLHC_dist']

    TWAP_df['TWAP_price']=0.5*(TWAP_df['OHLC_twap']+TWAP_df['OLHC_twap'])
    historical_price_total_df['TWAP_price']=TWAP_df['TWAP_price']
    historical_price_total_df['TWAP_price'].fillna(historical_price_total_df['Close'], inplace=True)    
    return historical_price_total_df