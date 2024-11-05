from api_wrappers.api import met_office_api
import json
class WeatherDataAPI:
    latitude = 53.800755
    longitude = -1.549077


    def get_data(self):
        data = met_office_api.retrieve_forecast(self.latitude, self.longitude)

        return json.loads(data.text)