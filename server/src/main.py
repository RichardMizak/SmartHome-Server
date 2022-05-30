"""
    Python flask Server
    Author: Richard Mižák
    Data: January 2022
"""
# Imports
from post import post
from flask import Flask,request,json
app = Flask(__name__)


# Functions
@app.route("/lights", methods=['GET', 'POST'])
def lights_get():
  """
        Function reads, withdraw data received from http POST request and rewrite the config file.
        Then call function to POST request.
        :return: success
    """
  x=request.data # Getting request from app
  new_json=x.decode('utf-8')
  y=json.loads(new_json)
  with open("config.json", "w") as outfile:
    json.dump(y, outfile)  # Saving signal into config.json file
  print(y)
 # s1 = post  # Calling post class for sending POST request
 # s1.send_request(self=s1)
  return  "success", 200


if __name__ == "__main__":
  app.run(host="0.0.0.0")