import requests
import json
import pandas as pd
import matplotlib as plt
import logging 


app_loger = logging.getLogger("App_logger")
app_loger.level(logging.DEBUG)

def gather_Data() -> pd.DataFrame:
    '''
    This function call Weather API to collect the weaher forcat every 3 hours for 5 days

    Parameters: 
        None.
    Exceptions:

    Retuen: 
        data frame object.
    '''
    app_loger.info("calling Weather API to fitch data.")

def drow_data(weather_data) -> None:
    '''
    This function plot the weather data using matplotlib.

    Parameters:
        weather_data (Dict): weather data forcast every 3 hours for 5 days.  
    Exceptions:

    Return: None.

    '''
    ...

def record_data(weather_data)-> None:
    '''
    This function write the weather forcast data to a json file
    
    parameters:
        weather_data (Dict): weather data forcast every 3 hours for 5 days. 
    Exception:

    Return: None.
    '''
    pass

def main():
    weather_data= gather_Data()
    ...

if __name__ == "__main__":
    main()