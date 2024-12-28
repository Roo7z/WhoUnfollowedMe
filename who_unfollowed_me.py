import json

# followers
f = open("followers_1.json")
data = json.load(f)

follower = []

for i in data:
    for j in i["string_list_data"]:
        follower.append(j["value"])

# following
f = open("following.json")
data = json.load(f)

following = []

for i in data["relationships_following"]:
    for j in i["string_list_data"]:
        following.append(j["value"])

# main
goodpeople = []

for i in following:
    if i in follower:
        goodpeople.append(i)

with open("unfollowers.txt", "w") as file:
    for i in following:
        if i not in goodpeople:
            file.write("https://www.instagram.com/" + i + "\n")

print("Daftar unfollowers telah disimpan di unfollowers.txt")
