# COVID-19 Global Data Tracker
# Data Analysis Report

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os
from datetime import datetime

# Set up visualization styles and output directory
sns.set(style='whitegrid')
plt.style.use('fivethirtyeight')
os.makedirs('outputs/plots', exist_ok=True) 

def main():
    try:
        # 1. Data Loading & Exploration
        df = pd.read_csv('owid-covid-data.csv')
        
        print("\nData Exploration:")
        print(f"Dataset dimensions: {df.shape}")
        print("\nMissing values (top 10):")
        print(df.isnull().sum().sort_values(ascending=False)[:10])

        # 2. Data Cleaning
        countries = ['Kenya', 'United States', 'India', 'Brazil', 'Germany']
        df_clean = df[df['location'].isin(countries)].copy()
        df_clean['date'] = pd.to_datetime(df_clean['date'])
        df_clean = df_clean.sort_values('date')

        # Handle missing values
        cols_to_fill = ['total_cases', 'total_deaths', 'people_vaccinated']
        df_clean[cols_to_fill] = df_clean.groupby('location')[cols_to_fill].ffill()
        df_clean = df_clean.dropna(subset=['total_cases', 'total_deaths', 'population'])

        # 3. EDA Visualizations
        # Cases over time
        plt.figure(figsize=(14, 7))
        for country in countries:
            country_data = df_clean[df_clean['location'] == country]
            plt.plot(country_data['date'], country_data['total_cases'], label=country)
        
        plt.title('COVID-19 Cases Over Time')
        plt.xlabel('Date')
        plt.ylabel('Total Cases')
        plt.legend()
        plt.savefig('outputs/plots/cases_over_time.png') 
        plt.close() 

        # Death rate analysis
        df_clean['death_rate'] = (df_clean['total_deaths'] / df_clean['total_cases']) * 100
        latest_data = df_clean.groupby('location').last().reset_index()

        plt.figure(figsize=(10, 6))
        sns.barplot(x='location', y='death_rate', data=latest_data)
        plt.title('Case Fatality Rate by Country')
        plt.ylabel('Fatality Rate (%)')
        plt.savefig('outputs/plots/fatality_rate.png')
        plt.close()

        # 4. Vaccination Analysis
        plt.figure(figsize=(14, 7))
        for country in countries:
            country_data = df_clean[df_clean['location'] == country]
            plt.plot(country_data['date'], 
                    country_data['people_vaccinated_per_hundred'], 
                    label=country)
        
        plt.title('Vaccination Coverage (% Population)')
        plt.xlabel('Date')
        plt.ylabel('Vaccinated Population (%)')
        plt.legend()
        plt.savefig('outputs/plots/vaccination_coverage.png')
        plt.close()

        # 5. Choropleth Map (Save as HTML)
        latest_global = df.groupby('iso_code').last().reset_index()
        fig = px.choropleth(latest_global,
                          locations="iso_code",
                          color="total_cases_per_million",
                          hover_name="location",
                          color_continuous_scale=px.colors.sequential.Plasma,
                          title="Global COVID-19 Case Distribution")
        fig.write_html("outputs/global_cases_map.html")  

        print("\nYay! Analysis complete! Check the 'outputs' folder for results.")

    except FileNotFoundError:
        print("Error: CSV file not found. Please download the dataset.")
    except KeyError as e:
        print(f"Error: Missing required column - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()