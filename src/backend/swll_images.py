import uuid

class Swll_Images:
    # Class attribute
    species = "SWLL Chart"

    

    aam_swll_url = 'http://www.meteoam.it/'

    def __init__(self, validity_utc, image_link, active):
        self.validity_utc = validity_utc
        self.image_link = image_link
        self.active = active
        self.uuid = str(uuid.uuid1())

    def get_validity(self):
        return self.validity_utc

    def get_image_link(self):
        return 'http://www.meteoam.it' + self.image_link

    def get_active(self):
        return self.active

    def get_uuid(self):
        return self.uuid

    def get_url_image_uuid(self):
        return "%s.gif" % self.uuid

    def __str__(self):
        value = "Validity: %s \n\
Link: %s \n\
Active: %s" % (
                     self.validity_utc, 
                     self.image_link,
                     self.active)
        return value