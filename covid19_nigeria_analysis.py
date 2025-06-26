import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
url = 'https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv'
df = pd.read_csv(url)

# Filter for Nigeria
nigeria_df = df[df['Country'] == 'Nigeria']

# Convert date column to datetime
nigeria_df['Date'] = pd.to_datetime(nigeria_df['Date'])

# Plotting the data
plt.figure(figsize=(12, 6))
plt.plot(nigeria_df['Date'], nigeria_df['Confirmed'], label='Confirmed Cases', color='blue')
plt.plot(nigeria_df['Date'], nigeria_df['Recovered'], label='Recovered Cases', color='green')
plt.plot(nigeria_df['Date'], nigeria_df['Deaths'], label='Deaths', color='red')
plt.title('COVID-19 Trends in Nigeria')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('nigeria_covid19_trend.png')  # Saves the plot
plt.show()
