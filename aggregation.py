def aggregate_daily_weather(weather_data):
    timestamp = weather_data[0]['timestamp']
    avg_temp = sum(entry['temp'] for entry in weather_data) / len(weather_data)
    max_temp = max(entry['temp'] for entry in weather_data)
    min_temp = min(entry['temp'] for entry in weather_data)

    conditions = [entry['condition'] for entry in weather_data]
    dominant_condition = max(set(conditions), key=conditions.count)
    
    humidity = weather_data[0]['humidity']
    wind_speed = weather_data[0]['wind_speed']
    
    return timestamp, avg_temp, max_temp, min_temp, dominant_condition, humidity, wind_speed


