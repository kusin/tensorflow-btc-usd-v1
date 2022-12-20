import pandas as pd;

# func set range year
def set_year(df_year):

    	
    #df_year.index = pd.to_datetime(df_year.index)
    #df_year = df_year.groupby(pd.Grouper(freq="M")).mean();
    #df_year = df_year.iloc[(df_year.index >= '2015-01-01') & (df_year.index <= '2015-12-31')];
    
    #df_year =  df_year.resample("M").sum();
    
    
    return df_year.index.dt.strftime("%Y/%m/%d").resample("M").sum();