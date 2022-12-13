#test conversations usage
# Macy Lakey and Lan-Anh Dang-Vu and Delaney Harwell
# mjlakey@uci.edu and ldangvu@uci.edu and dharwell@uci.edu
# 47566598 and 43785070 and 74084784
#
from pathlib import Path
from ds_messenger import DirectMessenger

path = Path('/Users/macyj/Desktop/a6/bollocks.dsu')
DM = DirectMessenger(username='boingboing1234', password='jumpywumpy213')
DM.dm.profile.load_profile(path)
DM.retrieve_new()
DM.dm.profile.save_profile(path)
conversations, contacts =  DM.dm.create_convos()
print(conversations)
print(contacts)

# path = Path('/Users/macyj/Desktop/a6/laylafile.dsu')
# DM = DirectMessenger(username='laylaa435', password='handsomestars23')
# DM.send('what?', 'boingboing1234')
# DM.dm.create_dm()
# DM.send('do u wanna hang?', 'boingboing1234')
# DM.dm.create_dm()
# DM.dm.profile.save_profile(path)
# conversations, contacts =  DM.dm.create_convos()
# print(conversations)
# print(contacts)
