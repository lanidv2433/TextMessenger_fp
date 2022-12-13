#ds_messenger.py
# Macy Lakey and Lan-Anh Dang-Vu and Delaney Harwell
# mjlakey@uci.edu and ldangvu@uci.edu and dharwell@uci.edu
# 47566598 and 43785070 and 74084784
#
import ds_protocol
import ds_client
import json
from Profile import Profile, Conversation

class DirectMessage():
  def __init__(self):
    self.messenger = None
    self.recipient = None
    self.message = None
    self.timestamp = None #not sure if this is needed at all
    self.profile = Profile()
    self.convo = None

  def create_dm(self):
    message = {'messenger': self.messenger, 'recipient': self.recipient, 'message': self.message, 'timestamp': self.timestamp}
    self.profile.add_message(message)
    return message
  def create_convos(self):
    msglst = self.profile.get_messages()
    self.convo = Conversation(msglst)
    conversations, contacts = self.convo.CreateConvo()
    return conversations, contacts


class DirectMessenger:
  def __init__(self, dsuserver=ds_client.HOST, username=None, password=None):
    self.token = ds_client.send(dsuserver,ds_client.PORT,username,password)
    self.dm = DirectMessage()
    self.username = username

  def send(self, message:str, recipient:str) -> bool:
    '''Send server dm request, extract server response and return true if successful, false if failed.'''
    # self.dm.recipient = recipient
    # self.dm.message = message
    # self.dm.timestamp = time.time()
    srv_msg, user_msg = ds_protocol.dm(self.token, message, recipient)
    resp_type, json_obj = ds_protocol.extract_json(srv_msg)
    usermsg_dict = json.loads(user_msg)
    self.dm.messenger = self.username
    self.dm.recipient = usermsg_dict['directmessage']['recipient']
    self.dm.message = usermsg_dict['directmessage']['entry']
    self.dm.timestamp = usermsg_dict['directmessage']['timestamp']
    if resp_type == 'error':
        return False
    elif resp_type == 'ok':
        return True
		
  def retrieve_new(self) -> list:
    srv_msg= ds_protocol.unread(self.token, "new")
    resp_type, json_obj = ds_protocol.extract_json(srv_msg)
    messages = json_obj['response']['messages']
    for usermsg_dict in messages:
      self.dm.messenger = usermsg_dict['from']
      self.dm.recipient = self.username
      self.dm.message = usermsg_dict['message']
      self.dm.timestamp = usermsg_dict['timestamp']
      self.dm.create_dm()
    return messages
 
  def retrieve_all(self) -> list:
    srv_msg = ds_protocol.alldms(self.token, "all")
    resp_type, json_obj = ds_protocol.extract_json(srv_msg)
    messages = json_obj['response']['messages']
    for usermsg_dict in messages:
      self.dm.messenger = usermsg_dict['from']
      self.dm.recipient = usermsg_dict['from']
      self.dm.message = usermsg_dict['message']
      self.dm.timestamp = usermsg_dict['timestamp']
      self.dm.create_dm()
    return messages
