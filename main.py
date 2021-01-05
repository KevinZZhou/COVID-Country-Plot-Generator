# Imports
import numpy as np
import pandas as pd
from pandas.api.extensions import ExtensionArray
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.collections as matcoll
import datetime as dt

# Load in Our World in Data csv file of COVID-19 data
covid_csv: str = "owid-covid-data.csv"
covid_df: pd.DataFrame = pd.read_csv(covid_csv)

# Create an array of the different countries in the dataset
country_list: ExtensionArray = covid_df["location"].unique()

# While loop to get user input for the desired country
while True:
    print("List of countries:")
    print(country_list)
    user_input = input(
            "Enter the country that you want to generate a plot for: ")
    country = user_input.title()
    if country not in country_list:
        print("That country is not in the list.  Try again.")
        continue
    else:
        break

print(country)
