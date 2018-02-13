# facebook-graph-api-explorerimport json
import requests
token="EAACEdEose0cBAC18lZAZCD6Jh57lwPJiBFIMGfUwj7Cm6FmiUGc8Xp73ruZBzb4yym9LRj1wXZBnyujCHTYwFwVjralGvpkX302KGk07cxes4KvEyhjH5AjGBCPQ0YvnrIAxxkX1vzR6iFztfe0xH0cigNiO7YevG6RPDpPCWZA8t61M46JAk2HCHEEeB64Y5p0ZAZAKDL9agZDZD"

print("My Facebook profile details")
me="https://graph.facebook.com/v2.12/me?access_token="+token
request1=requests.get(me)
name_json=request1.json()
converted_name_json=json.dumps(name_json)
print(converted_name_json)                     
print("=================================================================================================")

print("My Facebook friends")
friends="https://graph.facebook.com/v2.12/me/friends?access_token="+token
request2=requests.get(friends)
name_json1=request2.json()
converted=json.dumps(name_json1)
friends_list=converted[315:719]                 #To refactoring the output in required format
print("\n".join(friends_list.split(",")))
print("Total friends on facebook: "+converted[748:751])
print("===================================================================================================")

print("my facebook likes")
likes="https://graph.facebook.com/v2.12/me?fields=id,name,likes,link&access_token="+token
request3=requests.get(likes)
converted1=request3.json()
converted1_json=json.dumps(converted1)
likes_list=converted1_json[510:700]
print("\n".join(likes_list.split(",")))
likes_list1=converted1_json[816:3027]
print("\n".join(likes_list1.split(",")))
