import re
from bs4 import BeautifulSoup
class SWLL_Adapter:
    """
        This adapter parse data from AM site into value object
    """

    def extract_validity_utc(self, cane) -> str:
        m = re.search(r'<p class=\"col-md-3\">(?P<validity>.*)<br', cane)
        return self.retrieve_only_text(m.groupdict()['validity'])

    def extract_active_chart(self, item) -> str:
        m = re.search(r'strong', item)
        if m is None:
            return False
        else:
            return True

    def extract_image_url(self, item) -> str:
        m = re.search(r'^.*<img src="(?P<url_image>.*)" width="160"/></a>.*', item, flags=re.MULTILINE)
        return self.retrieve_only_text(m.groupdict()['url_image'])

    def retrieve_only_text(self, html) -> str:
        soup = BeautifulSoup(html,'html.parser')
        return soup.get_text()

if __name__ == "__main__":
    adapter = SWLL_Adapter()
    cane = '<p class="col-md-3">Validità: 24-01-2021 00:00 UTC<br>\n<a href="/Storage/Catop/2021-01-24/CNMC_FAX_202101240000_ITALIA_SW@@@@@@_999100@@@@@@_000_000_@@@@.GIF" rel="lightbox-1390"><img src="/Storage/Catop/2021-01-24/CNMC_FAX_202101240000_ITALIA_SW@@@@@@_999100@@@@@@_000_000_@@@@.GIF" width="160"/></a></br></p>'
    print(adapter.extract_validity_utc(cane))
    print(adapter.extract_image_url(cane))