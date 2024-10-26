from sqlalchemy import create_engine, Column, Integer, String, Float, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

DATABASE_URL = 'postgresql://postgres:root@localhost:5432/weather_monitoring'
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class DailyWeatherSummary(Base):
    __tablename__ = 'daily_weather_summary'
    
    id = Column(Integer, primary_key=True)
    city_name = Column(String)
    date = Column(Integer)
    avg_temp = Column(Float)
    max_temp = Column(Float)
    min_temp = Column(Float)
    dominant_condition = Column(String)
    alert_triggered = Column(Boolean, default=False)
    humidity = Column(Float)
    wind_speed = Column(Float)

Base.metadata.create_all(engine)

def store_daily_summary(city, timestamp, avg_temp, max_temp, min_temp, condition, alert_triggered=False, humidity=0.0, wind_speed=0.0):
    summary = DailyWeatherSummary(
        city_name=city,
        date=timestamp,
        avg_temp=avg_temp,
        max_temp=max_temp,
        min_temp=min_temp,
        dominant_condition=condition,
        alert_triggered=alert_triggered,
        humidity= humidity,
        wind_speed=wind_speed  # Assuming wind speed is not provided in the given data
    )
    session = Session()  # Use session here to avoid potential multi-threading issues
    try:
        session.add(summary)
        session.commit()
        print(f"Inserted data for {city} into database.")
    except Exception as e:
        print(f"Failed to insert data for {city}: {e}")
        session.rollback()
    finally:
        session.close()