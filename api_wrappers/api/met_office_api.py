from settings import WEATHER_DATA_API_KEY

from metofficedatahub.multiple_files import MetOfficeDataHub


def init_data_source():
    return MetOfficeDataHub(client_id=WEATHER_DATA_API_KEY, client_secret="fake")

def get_data(datahub):
    datahub.download_all_files(order_ids=["test_order_id"])
    return datahub.load_all_files()