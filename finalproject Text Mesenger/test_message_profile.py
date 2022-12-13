#test_message_profile.py and messenger
# Macy Lakey and Lan-Anh Dang-Vu and Delaney Harwell
# mjlakey@uci.edu and ldangvu@uci.edu and dharwell@uci.edu
# 47566598 and 43785070 and 74084784
#
from Profile import Profile, Message
from ds_messenger import DirectMessage, DirectMessenger
'''Commented out bc of changes, but tests were done throughout whole process'''
# p = Profile()
# p.load_profile('/Users/lanidv/Downloads/a6-main 2/file.dsu')
# # p.dsuserver = '"168.235.86.101"'
# # p.username = 'lannimacydelaney'
# # p.password = '123passing123'
# print(p)
# messenger = DirectMessenger(username='lannimacydelaney', password='123passing123')
# print(messenger)
# msg = 'porty'
# messenger.send(msg, 'caio')
# print(messenger.dm.messenger)
# print(messenger.dm.recipient)
# print(messenger.dm.message)
# dictionary1 = messenger.dm.create_dm()
# p.add_message(dictionary1)
# print(dictionary1)
# messenger.send('potty', 'caio')
# dictionary2 = messenger.dm.create_dm()
# p.add_message(dictionary2)
# message_lst = p.get_messages()
# print(message_lst)

# # Save the profile
# p.save_profile('/Users/lanidv/Downloads/a6-main 2/file.dsu')


# Create a new object and load file
messenger = DirectMessenger(username='lannimacydelaney', password='123passing123')
messenger.dm.profile.load_profile('/Users/lanidv/Downloads/a6-main 2/file.dsu')
newmsgs = messenger.retrieve_new()
messenger.dm.profile.save_profile('/Users/lanidv/Downloads/a6-main 2/file.dsu')


# messenger.dm.profile.get_messages()
# for msg in newmsgs:
#     p1.add_message(messenger.dm.create_dm())
# message_lst = p1.get_messages()
# print(message_lst)

# messenger = DirectMessenger(username="moppy123", password='123pass876')
# messenger.dm.profile.load_profile('/Users/lanidv/Downloads/a6-main 2/send.dsu')
# messenger.send('heya hiya', 'lannimacydelaney')
# messenger.dm.create_dm()
# messenger.dm.profile.save_profile('/Users/lanidv/Downloads/a6-main 2/send.dsu')

