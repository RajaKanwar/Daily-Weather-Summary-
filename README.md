
### Real-Time Data Processing System for Weather Monitoring with Rollups and Aggregates

## Overview
The Real-Time Data Processing System for Weather Monitoring aims to collect, aggregate, and visualize weather data from various sources. The system supports rollups for efficient data storage and retrieval, enabling users to monitor weather trends and anomalies in real time.


## 🔗 Links
[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/RajaKanwar/Daily-Weather-Summary-.git)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/raja-kanwar)


## Features

- Fetch live weather data for cities.
- Store daily weather summaries in a PostgreSQL database.
- Trigger alerts if temperature exceeds user-defined thresholds.
- Aggregate weather data to calculate daily averages, maximums, and minimums.
- Visualization of daily summaries and alerts.

## Technologies Used
- **Programming Language**: Python
- **Database**: PostgreSQL
- **Data Visualization**: Matplotlib, Plotly
- **Libraries**: SQLAlchemy, Requests, Schedule



## Features

- Fetch live weather data for cities.
- Store daily weather summaries in a PostgreSQL database.
- Trigger alerts if temperature exceeds user-defined thresholds.
- Aggregate weather data to calculate daily averages, maximums, and minimums.
- Visualization of daily summaries and alerts.

## Technologies Used
- **Programming Language**: Python
- **Database**: PostgreSQL
- **Data Visualization**: Matplotlib, Plotly
- **Libraries**: SQLAlchemy, Requests, Schedule

## Data Model

The database consists of the following tables:

### WeatherData:
- **id**: SERIAL PRIMARY KEY
- **city_name**: VARCHAR
- **timestamp**: TIMESTAMP
- **temperature**: FLOAT
- **humidity**: FLOAT
- **wind_speed**: FLOAT

### API Integration
The application integrates with the OpenWeatherMap API to fetch the following weather parameters:

- main: Current weather condition (e.g., Rain, Snow, Clear).
- temp: Current temperature in Centigrade.
- feels_like: Perceived temperature in Centigrade.
- dt: Time of the data update (Unix timestamp).

### Data Processing and Analysis
- The system calls the OpenWeatherMap API at a configurable interval (e.g., every 5 minutes).
- It retrieves and parses the weather data for the specified metros in India (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad).

### Rollups and Aggregates
Daily Weather Summary:

- Roll up weather data daily.
    Calculate:
        Average temperature
        Maximum temperature
        Minimum temperature
        Dominant weather condition (based on frequency).
- Store the daily summaries in a database for further analysis.

### Alerting Mechanism
- User-configurable thresholds for temperature or specific weather conditions.
- Continuously track the latest weather data.
- Trigger alerts when thresholds are breached, displayed in the console or through an email notification system.

### Visualizations
- Implement visualizations to display daily weather summaries, historical trends, and triggered alerts.





## Installation

### Step 1: Create a Virtual Environment
On Windows:
```bash
python -m venv venv
```

### Step 2: Activate the Virtual Environment

```bash
Copy code
venv\Scripts\activate
```
### Step 3: install requirments Python packages
```bash
pip install -r requirements.txt

``` 

### Step : For run application
```bash
python app.python
``` 

## Functionality



-  Process Weather Data
Function: *process_weather()*
Fetches and processes weather data for specified cities.
-  Fetch Weather Data
Function: *fetch_weather_data(city)*
Retrieves current weather data for a given city.
-  Store Daily Summary
Function: *store_daily_summary()*
Stores the daily weather summary in the database.
-  Daily Weather Summary Class
Class: *DailyWeatherSummary()*
Represents the daily summary of weather data.
- Aggregate Daily Weather
Function: *aggregate_daily_weather(weather_data)*
Aggregates weather data for the day.
- Check for Alerts
Function: *check_for_alerts(weather_data)*
Checks for any weather alerts based on the data.
- Visualize Weather Data
Function: *visualize_all_cities_weather()*
Visualizes the weather data for all cities in graphical format.
## Screenshots

![Table Date](https://drive.google.com/file/d/1_Nn63cApMuorGtYBGFfb2PV4h-pmw6kR/view?usp=sharing)

![Visualization](https://drive.google.com/file/d/1rj7HiW4hdTj0EKhl99qE8-OzhvYbYN3F/view?usp=sharing)

