# ds_protocol.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Macy Lakey and Lan-Anh Dang-Vu and Delaney Harwell
# mjlakey@uci.edu and ldangvu@uci.edu and dharwell@uci.edu
# 47566598 and 43785070 and 74084784

import json
from collections import namedtuple
import socket
import ds_client
import time


# Namedtuple to hold the values retrieved from json messages.
# TODO: update this named tuple to use DSP protocol keys
DataTuple = namedtuple('DataTuple', ['foo','baz'])

def extract_json(json_msg:str) -> DataTuple:
  '''
  Call the json.loads function on a json string and convert it to a DataTuple object
  
  TODO: replace the pseudo placeholder keys with actual DSP protocol keys
  '''
  try:
    json_obj = json.loads(json_msg)
    resp_type = json_obj['response']['type'] #gets response type to know if it is an error or ok.
  except json.JSONDecodeError:
    print("Json cannot be decoded.")
  return DataTuple(resp_type, json_obj)

def join(msg):
    """Join server using socket and prints server welcome response when connected."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.settimeout(3) #times out the wait to connect
        client.connect((ds_client.HOST, ds_client.PORT))
        
        send = client.makefile('w')
        receive = client.makefile('r')
        
        send.write(msg + '\r\n')
        send.flush()
        
        srv_msg = receive.readline()
        print("Response", srv_msg)
        return srv_msg

# def post(token, message):
#     '''Convert user message to JSON format and posts it to server using join function.'''
#     message = json.dumps(message)
#     user_post = '{"token": "%s", "post": %s}' % (token, message)
#     print(user_post)
#     join(user_post)

# def bio(token, entry):
#     '''Get timestamp of bio, convert user bio to JSON format then send to server using join function.'''
#     timestamp = time.time()
#     user_bio = '{"token": "%s", "bio": {"entry": "%s", "timestamp": "%s"}}' % (token, entry, timestamp)
#     print(user_bio)
#     join(user_bio)

def dm(token, entry, recipient):
  timestamp = time.time()
  user_dm = '{"token":"%s", "directmessage": {"entry": "%s","recipient":"%s", "timestamp": "%s"}}' % (token, entry, recipient, timestamp)
  srv_msg = join(user_dm)
  return srv_msg, user_dm

def unread(token, dm="new"):
  user_unread = '{"token":"%s", "directmessage": "new"}' % (token)
  srv_msg = join(user_unread)
  return srv_msg

def alldms(token, dm="all"):
  user_dms = '{"token":"%s", "directmessage": "all"}' % (token)
  srv_msg = join(user_dms)
  return srv_msg

    
