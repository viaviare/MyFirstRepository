import time

def current_time_millis():
    return int(round(time.time() * 1000))

class Product:

    def __init__(self, product_name="Black Duck_%s" % current_time_millis(),
                 product_code="123dfdf",
                 date_from="01.01.2018",
                 date_to="01.01.2020",
                 keywords="keywords",
                 head_title="Head Title",
                 meta_desc = "Meta Description",
                 purchase_price="450",
                 prices_USD="350",
                 prices_EUR="270",
                 short_desc="Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                            "Suspendisse sollicitudin ante massa, eget ornare libero "
                            "porta congue.",
                 full_desc="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse \n "
                           "sollicitudin ante massa, eget ornare libero porta congue. Cras scelerisque\n "
                           " dui non consequat sollicitudin. Sed pretium tortor ac auctor molestie. Nulla \n"
                           "facilisi. Maecenas pulvinar nibh vitae lectus vehicula semper. Donec et aliquet \n"
                           "velit. Curabitur non ullamcorper mauris. In hac habitasse platea "):
        self.product_name = product_name
        self.product_code = product_code
        self.date_from = date_from
        self.date_to = date_to
        self.keywords = keywords
        self.head_title = head_title
        self.meta_desc = meta_desc
        self.short_desc = short_desc
        self.full_desc = full_desc
        self.purchase_price = purchase_price
        self.prices_USD = prices_USD
        self.prices_EUR = prices_EUR