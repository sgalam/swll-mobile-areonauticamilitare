import uuid

class Swll_Images:
    # Class attribute
    species = "SWLL Chart"

    

    aam_swll_url = 'http://www.meteoam.it/'

    def __init__(self, validity_utc, image_link, active, image_id):
        self.validity_utc = validity_utc
        self.image_link = image_link
        self.active = active
        self.image_id = image_id

    def get_validity(self):
        return self.validity_utc

    def get_image_link(self):
        return 'http://www.meteoam.it' + self.image_link

    def get_active(self):
        return self.active

    def get_image_id(self):
        return self.image_id

    def get_url_image_id(self):
        return "%s.gif" % self.image_id

    def __str__(self):
        value = "%s \n\
Link: %s \n\
Active: %s" % (
                     self.validity_utc, 
                     self.image_link,
                     self.active)
        return value