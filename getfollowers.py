from InstagramAPI import InstagramAPI
import time

username = input("Login: ")
password = input("Password: ")
insta = InstagramAPI(username, password)
insta.login()

mid = ''
id_list = []
go = True
insta.getProfileData()
user = insta.LastJson['user']['pk']
time.sleep(2)
insta.getUserFollowers(user)
uid = insta.LastJson['users'][21]['pk']
time.sleep(2)
while go:
    insta.getUserFollowers(uid, mid)
    temp = insta.LastJson
    for user in temp['users']:
        #print(f'Following {user["full_name"]} user id: {user["pk"]}')
        nameid = {
            "full_name": user["full_name"],
            "id": user["pk"],
            "username": user["username"]
        }
        id_list.append(nameid)
        # insta.follow(user['pk'])
        # print('...Followed')
    try:
        mid = temp['next_max_id']
    except:
        # Break the loop
        go=False
    time.sleep(2)

insta.logout()

for id in id_list:
    print(f'{id["full_name"]}: {id["id"]} {id["username"]}')