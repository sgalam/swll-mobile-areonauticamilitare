#!/usr/bin/python3
import sys
from pprint import pprint

import traceback


from swll_adapter import SWLL_Adapter
from swll_images import Swll_Images
from swll_parser import SWLL_Parser

from swll_output_generator import SWLL_Output

from swll_fetch_data import SWLL_Fetch_Data

try:
    data = SWLL_Parser.parse_html()

    swll_data = []

    counter = 0
    for item in data:
            counter += 1
            adapter = SWLL_Adapter()
            value = Swll_Images(
                adapter.extract_validity_utc(item),
                adapter.extract_image_url(item),
                adapter.extract_active_chart(item),
                counter
            )       
            SWLL_Fetch_Data.fetch_and_save_local_image(
                value.get_image_link(),
                value.get_url_image_id()
                )
            swll_data.append(value)
            print(value)
            print("----")

    out = SWLL_Output()
    out.generate_output(swll_data)
except Exception:
    print("Exception in user code:")
    print("-"*60)
    traceback.print_exc(file=sys.stdout)
    print("-"*60)
    out = SWLL_Output()
    out.general_error()


