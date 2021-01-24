#!/usr/bin/python3
import sys
from pprint import pprint


from swll_adapter import SWLL_Adapter
from swll_images import Swll_Images
from swll_parser import SWLL_Parser

from swll_output_generator import SWLL_Output

from swll_fetch_data import SWLL_Fetch_Data

data = SWLL_Parser.parse_html()

swll_data = []

for item in data:
        adapter = SWLL_Adapter()
        value = Swll_Images(
            adapter.extract_validity_utc(item),
            adapter.extract_image_url(item),
            adapter.extract_active_chart(item)
        )       
        SWLL_Fetch_Data.fetch_and_save_local_image(
            value.get_image_link(),
            value.get_url_image_uuid()
            )
        swll_data.append(value)
        print(value)
        print("----")

out = SWLL_Output()
out.generate_output(swll_data)

