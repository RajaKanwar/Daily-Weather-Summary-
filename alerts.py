ALERT_THRESHOLD_TEMP = 30  # Example threshold

def check_for_alerts(weather_data):
    high_temp_count = sum(1 for entry in weather_data if entry['temp'] > ALERT_THRESHOLD_TEMP)
    alert_triggered = False
    
    if high_temp_count >= 2:  # If temp exceeds threshold for two consecutive updates
        alert_triggered = True
        print("ALERT: Temperature exceeded 30°C for two consecutive updates!")
    
    return alert_triggered
