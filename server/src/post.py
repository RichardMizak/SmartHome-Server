"""
    Python flask Server
    Author: Richard Mižák
    Data: January 2022
"""

# Imports
import requests

class post:
    """
        Class for POST request function
    """
    def send_request(self):
        """
               Function reads and withdraw data from config file and send them with http POST request.
               :return: success
           """
        url="http://192.168.0.107:80/signal" # URL of ESP8266 micro webserver
        with open('config.json', 'r') as openfile:
            json_object = openfile.read()    # Reading config.json file
            print(json_object)
        send=requests.post(url=url,data=json_object) # Sending POST request to ESP8266
        print(json_object)
        return "success", 200