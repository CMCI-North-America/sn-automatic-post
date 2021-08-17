

# Imports
import requests
from requests.api import post


# Your access keys
page_id = 603162579808366
fb_token = 'EAADViZAvYSB8BAGSV7i6dJiWRIEcJkdSEipytNtM0XYe95EnSlW2PGNDa5TVzXkzwdYPOCZABik8cX6CdcZCGjMgjv0eptgtW71ke9rvmudf3AHNonnZBNT8MLrAJLhvv2N5YbQpcU9F1ZBljsTqgCP4LFjAcmh2cRQcN2CL6YhzJjr5sPXZCPqb19Jl150AV4tHgKv57PrAZDZD'


# Send static post
def post_message(message):
    post_url = 'https://graph.facebook.com/{}/feed'.format(page_id)

    payload = {
    'message': message,
    'access_token': fb_token
    }

    return post_url, payload

# Send dynamic post
def post_message(message):
    post_url = 'https://graph.facebook.com/{}/photo'.format(page_id)
    media_location = ''

    payload = {
    'media': media_location,
    'access_token': fb_token
    }

    return post_url, payload

# Send post
# Takes in parameters url & data
r = requests.post()
print("Sent")