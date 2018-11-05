import vk_api

login, password = 'your@email.com', 'yourpassword'

vk_session = vk_api.VkApi(login, password)
vk_session.auth(token_only = True)

vk = vk_session.get_api()

num = 1000

buf = vk.polls.getVoters(owner_id = -56106344, poll_id = 309967436, answer_ids = 1042779310, count = num)

i = 0
arr = list()
while i < num:
	arr.append(buf[0]['users']['items'][i])
	i+=1

param = {'sex, city'}
# for elem in arr:
# 	man = vk.users.get(user_ids = elem, fields = param)
# 	try:
# 		print(man[0]['first_name'] + ' ' + man[0]['last_name'] + ' ' + str(man[0]['city']['id']) + ' ' + man[0]['city']['title'])
# 	except BaseException:
# 		continue

for elem in arr:
	man = vk.users.get(user_ids = elem, fields = param)
	try:
		if  str(man[0]['city']['id']) == '1':
			print(man[0]['first_name'] + ' ' + man[0]['last_name'])
	except BaseException:
		continue