import vk_api

login, password = 'your@email.com', 'yourpassword'

vk_session = vk_api.VkApi(login, password)
try:
	vk_session.auth(token_only = True)
except vk_api.AuthError as error_msg:
	print(error_msg)

vk = vk_session.get_api()

num = 1000

buf = vk.polls.getVoters(owner_id = -56106344, poll_id = 309967436, answer_ids = 1042779310, count = num)

i = 0
arr = list()
while i < num:
	arr.append(buf[0]['users']['items'][i])
	i+=1


