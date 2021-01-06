'''
This Python code takes user input for a country name and outputs a Matplotlib 
plot of COVID-19 cases and deaths for the specified country.

List of valid countries for user input:
['Afghanistan' 'Albania' 'Algeria' 'Andorra' 'Angola'
 'Antigua and Barbuda' 'Argentina' 'Armenia' 'Australia' 'Austria'
 'Azerbaijan' 'Bahamas' 'Bahrain' 'Bangladesh' 'Barbados' 'Belarus'
 'Belgium' 'Belize' 'Benin' 'Bhutan' 'Bolivia' 'Bosnia and Herzegovina'
 'Botswana' 'Brazil' 'Brunei' 'Bulgaria' 'Burkina Faso' 'Burundi'
 'Cambodia' 'Cameroon' 'Canada' 'Cape Verde' 'Central African Republic'
 'Chad' 'Chile' 'China' 'Colombia' 'Comoros' 'Congo' 'Costa Rica'
 "Cote d'Ivoire" 'Croatia' 'Cuba' 'Cyprus' 'Czechia'
 'Democratic Republic of Congo' 'Denmark' 'Djibouti' 'Dominica'
 'Dominican Republic' 'Ecuador' 'Egypt' 'El Salvador' 'Equatorial Guinea'
 'Eritrea' 'Estonia' 'Eswatini' 'Ethiopia' 'Fiji' 'Finland' 'France'
 'Gabon' 'Gambia' 'Georgia' 'Germany' 'Ghana' 'Greece' 'Grenada'
 'Guatemala' 'Guinea' 'Guinea-Bissau' 'Guyana' 'Haiti' 'Honduras'
 'Hong Kong' 'Hungary' 'Iceland' 'India' 'Indonesia' 'International'
 'Iran' 'Iraq' 'Ireland' 'Israel' 'Italy' 'Jamaica' 'Japan' 'Jordan'
 'Kazakhstan' 'Kenya' 'Kosovo' 'Kuwait' 'Kyrgyzstan' 'Laos' 'Latvia'
 'Lebanon' 'Lesotho' 'Liberia' 'Libya' 'Liechtenstein' 'Lithuania'
 'Luxembourg' 'Madagascar' 'Malawi' 'Malaysia' 'Maldives' 'Mali' 'Malta'
 'Marshall Islands' 'Mauritania' 'Mauritius' 'Mexico' 'Moldova' 'Monaco'
 'Mongolia' 'Montenegro' 'Morocco' 'Mozambique' 'Myanmar' 'Namibia'
 'Nepal' 'Netherlands' 'New Zealand' 'Nicaragua' 'Niger' 'Nigeria'
 'North Macedonia' 'Norway' 'Oman' 'Pakistan' 'Palestine' 'Panama'
 'Papua New Guinea' 'Paraguay' 'Peru' 'Philippines' 'Poland' 'Portugal'
 'Qatar' 'Romania' 'Russia' 'Rwanda' 'Saint Kitts and Nevis' 'Saint Lucia'
 'Saint Vincent and the Grenadines' 'Samoa' 'San Marino'
 'Sao Tome and Principe' 'Saudi Arabia' 'Senegal' 'Serbia' 'Seychelles'
 'Sierra Leone' 'Singapore' 'Slovakia' 'Slovenia' 'Solomon Islands'
 'Somalia' 'South Africa' 'South Korea' 'South Sudan' 'Spain' 'Sri Lanka'
 'Sudan' 'Suriname' 'Sweden' 'Switzerland' 'Syria' 'Taiwan' 'Tajikistan'
 'Tanzania' 'Thailand' 'Timor' 'Togo' 'Trinidad and Tobago' 'Tunisia'
 'Turkey' 'Uganda' 'Ukraine' 'United Arab Emirates' 'United Kingdom'
 'United States' 'Uruguay' 'Uzbekistan' 'Vanuatu' 'Vatican' 'Venezuela'
 'Vietnam' 'World' 'Yemen' 'Zambia' 'Zimbabwe']
'''

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
    user_input: str = input(
            "Enter the country that you want to generate a plot for: ")
    country: str = user_input.title()
    # Use the array of different countries to check if the user input is valid
    # Continue to loop if the input is invalid
    if country not in country_list:
        print("That country is not in the list.  Try again.")
        continue
    # Exit the while loop otherwise
    else:
        break

# Get a list of dates for the specified country - Used as x-values
ds: list = covid_df[covid_df["location"] == country]['date']
dates: list = [dt.datetime.strptime(d, "%Y-%m-%d").date() for d in ds]

# Get lists of 4 important statistics for the specified country:
    # Total COVID-19 cases
    # New daily COVID-19 cases
    # Total COVID-19 deaths
    # New daily COVID-19 deaths
total_cases: list = covid_df[covid_df["location"] == country]["total_cases"]
total_deaths: list = covid_df[covid_df["location"] == country]["total_deaths"]
new_cases: list = covid_df[covid_df["location"] == country]["new_cases"]
new_deaths: list = covid_df[covid_df["location"] == country]["new_deaths"]

# Set up the main plot with 4 subplots
fig, axes = plt.subplots(2, 2, figsize = (20, 12))
fig.suptitle("COVID-19 Visualizations: " + country, fontsize = 30)

# Set up the total COVID-19 cases subplot
axes[0, 0].plot(dates, total_cases)
axes[0, 0].set_title("Total Cases in " + country)
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Cases")

# Set up the total COVID-19 deaths subplot
axes[0, 1].plot(dates, total_deaths)
axes[0, 1].set_title("Total Deaths in " + country)
axes[0, 1].set_xlabel("Date")
axes[0, 1].set_ylabel("Deaths")

# Set up the new daily COVID-19 cases subplot
axes[1, 0].plot(dates, new_cases)
axes[1, 0].set_title("Daily Cases in " + country)
axes[1, 0].set_xlabel("Date")
axes[1, 0].set_ylabel("Cases")

# Set up the new daily COVID-19 deaths subplot
axes[1, 1].plot(dates, new_deaths)
axes[1, 1].set_title("Daily Deaths in " + country)
axes[1, 1].set_xlabel("Date")
axes[1, 1].set_ylabel("Deaths")

# Export the plot as a png image
file_name: str = country.replace(" ", "-")
fig.savefig("plots/" + file_name + ".png", bbox_inches = "tight")