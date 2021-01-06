# COVID-Country-Plot-Generator

## Description
With the COVID-19 pandemic impacting various regions around the world, I wanted to find a way to monitor how different countries have handled/are handling the virus.  As such, I created this Python project, which generates a plot of COVID cases and deaths in a user-specified country.  This is a useful way to quickly visualize a country's status during the pandemic.

The project uses a csv file from [Our World in Data](https://ourworldindata.org/), whose mission is to focus on large global issues such as poverty, inequality, and climate change through a data and research driven perspective.  Our World in Data has done an excellent job in compiling data on the impact of COVID-19 on countries from around the world and visualizing it, which can be found [here](https://ourworldindata.org/coronavirus).

To get the visualization, run main.py, and you will be prompted in the terminal for a country name (a list of valid country names is provided at the top of main.py).  Once a valid name is selected, the program will automatically save a png image for that country in the plots folder. The

#### Example
![South Korea](/plots/South-Korea.png)

## Technologies Used
This project was coded in Python and uses NumPy, pandas, and Matplotlib.

## Setup
First, make sure that you have Python installed on your device.  This project uses Python 3.9.1, but should work for Python 3.5+ (type hinting).
If Python is installed on your system using the Anaconda distribution, then you should already have the requisite packages installed and do not to install anything else.
If you are not using Anaconda, check to see if you have previously installed NumPy, pandas, and Matplotlib.  Otherwise, enter the following into the command line:
```sh
$ pip install numpy
$ pip install pandas
$ pip install matplotlib
```
A [virtual environment](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/) is optional.

Download the files onto your system, either by downloading it directly in the browser or entering the following into the command line:
```sh
$ git clone https://github.com/KevinZZhou/COVID-Country-Plot-Generator.git
```
After this, run main.py within an IDE or navigate to the project directory and enter the following in the command line:
```sh
$ python main.py
```