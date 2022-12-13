#test_ds_messenger.py
# Macy Lakey and Lan-Anh Dang-Vu and Delaney Harwell
# mjlakey@uci.edu and ldangvu@uci.edu and dharwell@uci.edu
# 47566598 and 43785070 and 74084784
#
from ds_messenger import DirectMessage, DirectMessenger

print('Testing DirectMessenger\n')
dm1 = DirectMessenger(username="lannimacy2", password="123pass")
token1 = dm1.token
print('lannimacy2 token = ', token1)

print('\n lannimacy2 sending message to mufasalada')
TorF = dm1.send("mufasa where r u", 'mufasalada')
if TorF == True:
    print('message successfully sent!')
elif TorF == False:
    print('message failed to send :(')


dm2 = DirectMessenger(username="mufasalada", password="123pass4523")
token2 = dm2.token
print('mufasalada token = ', token2)

print('\nMufasa logs in and checks new messages')
messages = dm2.retrieve_new()
print('Here are your new messages:', messages)

print("\nPrinting all messages:")
messages = dm2.retrieve_all()
print(messages)

print('Testing DirectMessage')
print(dm1.dm.recipient)
print(dm1.dm.message)
print(dm1.dm.timestamp)



