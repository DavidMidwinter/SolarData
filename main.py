from api_wrappers import weather_data_wrapper
import json
weatherData = weather_data_wrapper.WeatherDataAPI()

print(json.dumps(weatherData.get_data(), indent=4))
