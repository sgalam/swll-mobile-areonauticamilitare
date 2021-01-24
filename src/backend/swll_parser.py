from bs4 import BeautifulSoup

from swll_fetch_data import SWLL_Fetch_Data


class SWLL_Parser:
    """
    This class parse html from outside
    """
    @staticmethod
    def parse_html():
        soup = BeautifulSoup(SWLL_Fetch_Data.fetch_data(), 'html.parser')

        # todo servira?
        description = soup.find_all('p')[2]

        # todo servira?
        charts_validity = soup.find_all('p')[3]


        range_charts = [4,5,6,7]
        chart = 0
        charts_available = []

        for chart in range_charts:
                item = str(soup.find_all('p')[chart])
                charts_available.append(item)

        return charts_available