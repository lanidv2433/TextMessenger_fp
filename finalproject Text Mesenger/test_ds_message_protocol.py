#testing ds_protocol
# Macy Lakey and Lan-Anh Dang-Vu and Delaney Harwell
# mjlakey@uci.edu and ldangvu@uci.edu and dharwell@uci.edu
# 47566598 and 43785070 and 74084784
#
import ds_protocol

print("lannimacy join server")
joining = '{"join": {"username": "%s","password": "%s", "token": ""}}' % ("lannimacy2", "123pass")
srv_msg = ds_protocol.join(joining)
resp_type, json_obj = ds_protocol.extract_json(srv_msg)
token1 = json_obj['response']['token']
print('lannimacy2 token', token1)
input('Continue')

print("\nmufasalada joins server")
joining = '{"join": {"username": "%s","password": "%s", "token": ""}}' % ("mufasalada", "123pass4523")
srv_msg = ds_protocol.join(joining)
resp_type, json_obj = ds_protocol.extract_json(srv_msg)
token2 = json_obj['response']['token']
print('mufasalada token', token2)
input('Continue')

print("\nlannimacy send 'Hey mufasalada' to mufasa")
ds_protocol.dm(token1, "Heya mufasalada!", 'mufasalada')
input('Continue')

print("\nmufasa reads their messages")
ds_protocol.unread(token2, "new")
ds_protocol.alldms(token2, "all")
input('Continue')

print("\nmufasa replies to lannimacy 'wassup lannimacy'")
ds_protocol.dm(token2, "Wassup lannimacy", "lannimacy2")
input("Continue")

print('\nlannimacy read message')
ds_protocol.unread(token1, "new")
ds_protocol.alldms(token1, "all")
input('Continue')

print("\nMufasa sends another message 'wanna hang l8r'")
ds_protocol.dm(token2, "Wanna hang l8r?", "lannimacy2")
input('Continue')

print('\nlannimacy read second message')
ds_protocol.unread(token1, "new")
ds_protocol.alldms(token1, "all")
