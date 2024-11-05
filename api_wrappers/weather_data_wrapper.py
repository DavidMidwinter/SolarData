from api import met_office_api
class WeatherDataAPI:

    datahub = None

    def __init__(self):
        self.datahub = met_office_api.init_data_source()

    def get_data(self):
        data = met_office_api.get_data(self.datahub)
        return data