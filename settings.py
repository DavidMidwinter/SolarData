import configparser
config_file = "settings.ini"
config = configparser.ConfigParser()

config.read(config_file)

WEATHER_DATA_API_KEY = config.get("weather_data_service", "WEATHER_DATA_API_KEY")
WEATHER_DATA_URL = config.get("weather_data_service", "WEATHER_DATA_URL")