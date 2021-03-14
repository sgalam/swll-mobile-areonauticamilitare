import requests

class SWLL_Fetch_Data:
    """
        This class fetch data from outside
    """
    @staticmethod
    def fetch_data():
        user_agent = {'User-agent': 'Mozilla/5.0'}
        url = 'http://www.meteoam.it/prodotti_grafici/bassiStrati'
        response  = requests.get(url, headers = user_agent)
        return response.content

    @staticmethod
    def fetch_image(url_image):
        user_agent = {'User-agent': 'Mozilla/5.0', 'referer': 'http://www.meteoam.it/prodotti_grafici/bassiStrati'}

        response  = requests.get(url_image, headers = user_agent)
        return response.content
    
    @staticmethod
    def fetch_and_save_local_image(url_image_remote, uri_image_local):
        file = SWLL_Fetch_Data.fetch_image(url_image_remote)
        print(url_image_remote)
        with open('/dist/am_charts/%s' % uri_image_local, 'wb') as f:
           f.write(file)       