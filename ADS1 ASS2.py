#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 20:25:44 2023

@author: kamalib
"""

#import important libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def read_data(filename):
    # Read the data from the file into a DataFrame, skipping unnecessary initial columns
    data = pd.read_csv(filename, skiprows=3)

    # Drop unnecessary columns: Country Code, Indicator Name, Indicator Code
    data.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis=1, inplace=True)

    # Set 'Country Name' as the index
    data.set_index('Country Name', inplace=True)

    # Transpose the DataFrame to have years as columns and countries as rows
    transposed_data = data.T

    # Create two separate dataframes: one with years as columns and one with countries as columns
    years_df = transposed_data.copy()
    countries_df = transposed_data.transpose().copy()

    return years_df, countries_df

# Read Urban Population
# Filename stores the path of the file to be read
filename = '//Users/kamalib/Downloads/Datasets/API_SP.URB.TOTL.IN.ZS_DS2_en_csv_v2_5996759.csv'

#Call the read_data function for specific file
urban_years_df, urban_countries_df = read_data(filename)

# Printing the first few rows of the dataframes
print("Years DataFrame:")
urban_years_df.head()
print("\nCountries DataFrame:")
urban_countries_df.head()

#Read Green House Emission
# Filename stores the path of the file to be read
filename = '//Users/kamalib/Downloads/Datasets/API_EN.ATM.GHGT.KT.CE_DS2_en_csv_v2_5995567.csv'

#Call the read_data function for specific file
greenhouse_years_df, greenhouse_countries_df = read_data(filename)

#Read Arable Land(%)
# Filename stores the path of the file to be read
filename = '//Users/kamalib/Downloads/Datasets/API_AG.LND.ARBL.ZS_DS2_en_csv_v2_5995308.csv'

#Call the read_data function for specific file
arable_land_years_df, arable_land_countries_df = read_data(filename)


#Forest Land(%)
# Filename stores the path of the file to be read
filename = '//Users/kamalib/Downloads/Datasets/API_AG.LND.FRST.ZS_DS2_en_csv_v2_5994693.csv'

#Call the read_data function for specific file
forest_land_years_df, forest_land_countries_df = read_data(filename)


#Agriculture Land(%)
# Filename stores the path of the file to be read
filename = '//Users/kamalib/Downloads/Datasets/API_AG.LND.AGRI.ZS_DS2_en_csv_v2_5995314.csv'

#Call the read_data function for specific file
agr_land_years_df, agr_land_countries_df = read_data(filename)

#Access to Electricity(%)
# Filename stores the path of the file to be read
filename = '//Users/kamalib/Downloads/Datasets/API_EG.ELC.ACCS.ZS_DS2_en_csv_v2_5995100.csv'

#Call the read_data function for specific file
elc_acc_years_df, elc_acc_countries_df = read_data(filename)

#Population Growth(%)
# Filename stores the path of the file to be read
filename = '//Users/kamalib/Downloads/Datasets/API_SP.POP.GROW_DS2_en_csv_v2_5995052.csv'

#Call the read_data function for specific file
pop_years_df, pop_countries_df = read_data(filename)

#GDP(%)
# Filename stores the path of the file to be read
filename = '//Users/kamalib/Downloads/Datasets/API_NV.AGR.TOTL.ZS_DS2_en_csv_v2_5995988.csv'

#Call the read_data function for specific file
gdp_years_df, gdp_countries_df = read_data(filename)

#electricity Consumption(kwh)
# Filename stores the path of the file to be read
filename = '//Users/kamalib/Downloads/Datasets/API_EG.USE.ELEC.KH.PC_DS2_en_csv_v2_5995551.csv'

#Call the read_data function for specific file
elc_use_years_df, elc_use_countries_df = read_data(filename)

#Renewable electricity output(%)
# Filename stores the path of the file to be read
filename = '//Users/kamalib/Downloads/Datasets/API_EG.ELC.RNEW.ZS_DS2_en_csv_v2_5995544.csv'

#Call the read_data function for specific file
rnw_elc_years_df, rnw_elc_countries_df = read_data(filename)

#Renewable energy consumption(%)
# Filename stores the path of the file to be read
filename = '//Users/kamalib/Downloads/Datasets/API_EG.ELC.RNEW.ZS_DS2_en_csv_v2_5995544.csv'

#Call the read_data function for specific file
rnw_cnsmp_years_df, rnw_cnsmp_countries_df = read_data(filename)

#bargraph

def plot_filtered_data(countries_df, selected_countries, years, title):

    # Sort the rows (countries) alphabetically
    selected_countries.sort()

    # Filtering the data for the selected countries and years
    filtered_data = countries_df[selected_countries].loc[years]

    # Plotting a bar graph
    filtered_data.T.plot(kind='bar', figsize=(10, 6))  # Transpose for correct plotting orientation
    plt.title(title)
    plt.xlabel('Country Name')
    plt.legend(title='Year')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Selecting specified countries containing the greenhouse gas emissions data
selected_countries = ['China', 'India', 'Japan', 'Indonesia', 'Bangladesh', 'Afghanistan', 'Philippines', 'Thailand', 'Pakistan', 'Malaysia']

# Five-year increments
years = ['1990', '1995', '2000', '2005', '2010', '2015', '2020']

plot_filtered_data(greenhouse_years_df, selected_countries, years,'Greenhouse Gas Emissions (kt of CO2 equivalent)')

#display data in tabular format for the countries with their indicator values
def filter_urban_data(data, selected_countries, years):
    # Filtering the data for the selected countries and years
    filtered_data = data[selected_countries].loc[years]

    # Displaying the filtered data in tabular format
    print(filtered_data.T)

#Call the function to display urban population% for countries over the year
urban_years = ['1980', '2000','2020']
filter_urban_data(urban_years_df, selected_countries, urban_years)

def plot_arable_land(data, selected_countries, years, title):
    if 'Country Name' in data.index:
        # Filtering the data for the selected countries and years
        filtered_data = data.loc[selected_countries, years]
    else:
        # Filtering the data for the selected countries and years
        filtered_data = data[selected_countries]
        filtered_data = filtered_data.loc[years]

    # Plotting a line graph with dotted lines
    plt.figure(figsize=(10, 6))
    for country in selected_countries:
        plt.plot(filtered_data.index.astype(int), filtered_data.loc[:, country], linestyle='--', label=country)

    plt.title(title)
    plt.xlabel('Year')
    plt.grid(True)

    # Placing the legend outside the graph
    plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

elc_years = ['2000','2002', '2004', '2006', '2008', '2010','2012', '2014', '2016', '2018', '2020']
plot_arable_land(elc_acc_years_df, selected_countries, elc_years, 'Access to electricity Over Years')

rnw_year = ['1990','2000', '2010','2015']
plot_filtered_data(rnw_elc_years_df, selected_countries, rnw_year, 'Renewable electricity output (% of total electricity output)')

year = ['1960', '1965', '1970', '1975', '1980', '1985', '1990', '1995', '2000', '2005', '2010', '2015', '2020']  # Years of interest

plot_arable_land(arable_land_years_df, selected_countries, year, 'Arable Land Over Years')
plot_arable_land(forest_land_years_df, selected_countries, year, 'Forest Land Over Years')
plot_arable_land(agr_land_years_df, selected_countries, year, 'Agriculture Land Over Years')



def combine_indicator_data(*indicator_dfs):
    # Assign indicator names to the DataFrames
    indicator_names = ['Arable Land', 'Forest Land', 'Agriculture Land', 'Urban', 'Populution Growth', 'Access to Electricity', 'Electrcity Consumption', 'Renewabale Electricity', 'Renewable Consumption', 'Greenhouse Emission', 'GDP']
    named_indicator_dfs = zip(indicator_names, indicator_dfs)

    # Create a list to hold modified DataFrames with indicator names
    modified_dfs = []

    # Add indicator names to the DataFrames and append them to modified_dfs list
    for name, df in named_indicator_dfs:
        df['Indicator Name'] = name
        modified_dfs.append(df)

    # Merge the modified DataFrames on 'Country Name' index
    combined_data = pd.concat(modified_dfs)

    # Removing null values
    combined_data.dropna(axis=1, how='all', inplace=True)
    combined_data.dropna(axis=0, how='all', inplace=True)
    return combined_data

# Pass your indicator DataFrames as arguments below
combined_data = combine_indicator_data(arable_land_countries_df, forest_land_countries_df, agr_land_countries_df, urban_countries_df, pop_countries_df, elc_acc_countries_df, elc_use_countries_df, rnw_elc_countries_df, rnw_cnsmp_countries_df, greenhouse_countries_df, gdp_countries_df)
print(combined_data)

def extract_country_data(country_name, combined_data):
    country_data = combined_data[combined_data.index == country_name]

    # Dropping unnecessary columns (0th columns)
    country_data.drop(country_data.columns[0], axis=1, inplace=True)
    # Set 'Indicator Name' as index and drop unnecessary columns
    country_data.set_index('Indicator Name', inplace=True)

    # Removing null values
    country_data.dropna(axis=1, how='all', inplace=True)
    country_data.dropna(axis=0, how='all', inplace=True)

    return country_data

# Extracting data for 'China'
china_data = extract_country_data('China', combined_data)

def calculate_correlation_heatmap(country_data,name):
    # Transpose the data to calculate correlation between indicators
    transposed_data = country_data.T

    # Calculate the correlation matrix between indicators
    correlation_matrix = transposed_data.corr()

    # Create a heatmap for correlation between indicators
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap for '+ name)
    plt.show()

# Correlation function for 'China'
calculate_correlation_heatmap(china_data, "China")

# Extracting data for 'India'
India_data = extract_country_data('India', combined_data)
# Correlation function for 'India'
calculate_correlation_heatmap(India_data, "India")

# Extracting data for 'Afghanistan'
afg_data = extract_country_data('Afghanistan', combined_data)
# Correlation function for 'Afghanistan'
calculate_correlation_heatmap(afg_data,"Afghanistan")

china_data.describe()

India_data.describe()



# Selecting specified countries containing the greenhouse gas emissions data
selected_countries = ['Europe & Central Asia', 'South Asia', 'North America','Middle East & North Africa', 'South Africa', 'Arab World']

# Five-year increments
years = ['1990', '1995', '2000', '2005', '2010', '2015', '2020']

plot_filtered_data(greenhouse_years_df, selected_countries, years,'Greenhouse Gas Emissions (kt of CO2 equivalent)')

# Selecting specified countries containing the greenhouse gas emissions data
selected_countries = ['Europe & Central Asia', 'South Asia', 'North America','Middle East & North Africa', 'South Africa', 'Arab World']

# Five-year increments
years = ['1990', '1995', '2000', '2005', '2010', '2015', '2020']

plot_filtered_data(rnw_elc_years_df, selected_countries, years,'Renewable Electricity (%)')