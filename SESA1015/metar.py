# Created by YongHua - 24 Feb 2021
# METAR: METeorological Aerodrome Report


import re  # regular expression
import requests

class metar:
    def __init__(self, airport_code):
        if type(airport_code) != str:
            raise TypeError("Please enter a valid string.")
        self.airport_code = airport_code.upper()  # convert all letters into uppercase
        self.raw_metar = ""
        print("A METAR object has been created. ICAO Airport Code: {}".format(self.airport_code))
        print(self.get_metar(), '\n')


    def __repr__(self):
        return self.airport_code


    def get_metar(self):
        """
        Takes a string parameter 'airport_code' (ICAO airport code)
        and returns the latest raw METAR data. Needs internet connection.
        """

        url = "https://www.aviationweather.gov/metar/data?ids={}&format=raw&date=&hours=0".format(self.airport_code)
        page = requests.get(url)
        print("{}\tElapsed time: {}".format(page, page.elapsed))
        print('=' * (len(str(page)) + 18 + len(str(page.elapsed))))

        html_bytes = page.content
        html_string = html_bytes.decode('utf-8')

        if re.search("No METAR found for {}".format(self.airport_code), html_string):
            raise Exception("METAR not found. Please enter a existing or valid ICAO airport code.")

        # matches = re.finditer(airport_code, html_string)
        match_start = re.search("<code>{}".format(self.airport_code), html_string)
        match_end = re.search("</code>", html_string)
        start = match_start.span()[0]
        end = match_end.span()[1]
        result = html_string[start:end][6:-7]
        self.raw_metar = result
        return result


my_metar1 = metar("WMSA")  # Kuala Lumpur International Airport
my_metar2 = metar("EGLL")  # London Heathrow Airport
