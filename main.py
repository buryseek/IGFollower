import time

import instaloader

L = instaloader.Instaloader()

# Login or load session
username = "ki_fac"
password = "massmedia"
L.login(username, password)  # (login)


# Obtain profile metadata
f = open("usernames.txt", "r")
for user in f:
    user = user.replace("\n", '')
    print(user)
    profile = instaloader.Profile.from_username(L.context, user)

    # Print list of followees
    follow_list = []
    count = 0
    for followee in profile.get_followers():
        follow_list.append(followee.username)
        file = open(f"followers_list_{user}.txt", "a+")
        file.write(follow_list[count])
        file.write("\n")
        file.close()
        print(follow_list[count])
        count = count + 1
    time.sleep(500)
f.close()
