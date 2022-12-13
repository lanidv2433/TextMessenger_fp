# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Macy Lakey and Lan-Anh Dang-Vu and Delaney Harwell
# mjlakey@uci.edu and ldangvu@uci.edu and dharwell@uci.edu
# 47566598 and 43785070 and 74084784
#


import ds_protocol
#from NaClProfile import NaClProfile

PORT = 3021
HOST = "168.235.86.101"

def send(server:str, port:int, username:str, password:str): #message:str):
  '''
  The send function joins a ds server and sends a message, bio, or both
  :param server: The ip address for the ICS 32 DS server.
  :param port: The port where the ICS 32 DS server is accepting connections.
  :param username: The user name to be assigned to the message.
  :param password: The password associated with the username.
  :param message: The message to be sent to the server.
  :param bio: Optional, a bio for the user.
  '''
  #TODO: return either True or False depending on results of required operation
  #NaCl = NaClProfile()
  #keypair = NaCl.generate_keypair()
  #ourtoken = NaCl.public_key
  joining = '{"join": {"username": "%s","password": "%s", "token":""}}' % (username, password)
  srv_msg = ds_protocol.join(joining)
  resp_type, json_obj = ds_protocol.extract_json(srv_msg)
  if resp_type == 'error':
    print("Unable to get token because username/password are either taken or didn't fulfill server requirements")
    token = None
  else:
    token = json_obj['response']['token']
  return token
  
  #if message == '' or message == ' ': #Does not execute post function if message is empty or whitespace
    #pass
  #else:
    #ds_protocol.post(token, message)

    
    
