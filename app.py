import schedule
import time
from weather_api import fetch_weather_data
from aggregation import aggregate_daily_weather
from alerts import check_for_alerts
from database import store_daily_summary

CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

weather_records = {}
print(CITIES)
def process_weather():
    global weather_records
    for city in CITIES:
        weather = fetch_weather_data(city)
        if weather:
            if city not in weather_records:
                weather_records[city] = []
            weather_records[city].append(weather)
            
            print(f"length weather_records : {len(weather_records[city])}")
            
            print(f"city weather_records : {weather_records[city]}")
            
            if len(weather_records[city]) > 0 :  # Assuming 5 min intervals for 24 hours
                timestamp, avg_temp, max_temp, min_temp, dominant_condition, humidity, wind_speed  = aggregate_daily_weather(weather_records[city])
                alert_triggered = check_for_alerts(weather_records[city])
                
                store_daily_summary(city, timestamp, avg_temp, max_temp, min_temp, dominant_condition, alert_triggered, humidity, wind_speed)
                weather_records[city] = []  # Reset after processing

#schedule.every(10).minutes.do(process_weather)
process_weather()

if __name__ == "__main__":
    while True:

        time.sleep(1)
