import configparser
config_file = "settings.ini"
config = configparser.ConfigParser()

config.read(config_file)

WEATHER_DATA_API_KEY = config.get("api_keys", "WEATHER_DATA_API_KEY")