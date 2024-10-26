from sqlalchemy import func
from database import DailyWeatherSummary, Session
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def visualize_all_cities_weather():
    session = Session()
    
    # Fetch all daily summaries for all cities
    summaries = session.query(DailyWeatherSummary).all()
    
    if not summaries:
        print("No data found for any city.")
        session.close()
        return
    
    # Prepare data structure for visualization
    city_data = {}
    
    for summary in summaries:
        city = summary.city_name
        
        # Convert the Unix timestamp to a datetime object
        date = datetime.fromtimestamp(summary.date)  # Assuming summary.date is a Unix timestamp
        
        # Create timestamps for past and future dates
        past_date = date - timedelta(days=1)  # One day in the past
        future_date = date + timedelta(days=1)  # One day in the future
        
        avg_temp = summary.avg_temp

        # Organize data by city, including past and future dates
        if city not in city_data:
            city_data[city] = {'dates': [], 'avg_temps': []}
        
        # Append past date data
        city_data[city]['dates'].append(past_date)
        city_data[city]['avg_temps'].append(avg_temp)  # Adjust this as necessary
        
        # Append actual date data
        city_data[city]['dates'].append(date)
        city_data[city]['avg_temps'].append(avg_temp)
        
        # Append future date data
        city_data[city]['dates'].append(future_date)
        city_data[city]['avg_temps'].append(avg_temp)  # Adjust this as necessary

    # Plotting the data for each city
    plt.figure(figsize=(12, 6))

    for city, data in city_data.items():
        plt.plot(data['dates'], data['avg_temps'], marker='o', label=city)

    # Enhancing the plot
    plt.xlabel('Date (Month Day)')
    plt.ylabel('Average Temperature (°C)')
    plt.title('Temperature Trends for All Cities')

    # Formatting x-axis ticks to show month and day
    plt.xticks(data['dates'], [date.strftime('%b %d') for date in data['dates']], rotation=45)
    
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

    session.close()

# Call the function to visualize weather for all cities
visualize_all_cities_weather()
