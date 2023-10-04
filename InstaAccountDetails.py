import instaloader

ig = instaloader.Instaloader()
username = input("Enter username: ")
profile = instaloader.Profile.from_username(ig.context, username)

print("Username: ", profile.username)
print("Number of posts uploaded: ", profile.mediacount)
print(profile.username + " is having " + str(profile.followers) + " followers")
print(profile.username + " is following " + str(profile.followees) + " people")
print("Bio: ", profile.biography)
instaloader.Instaloader().download_profile(username, profile_pic_only=True)
