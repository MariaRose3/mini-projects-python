# Import instaloader package
import instaloader

# creating an Instaloader() object
ig=instaloader.Instaloader()

# Taking the instagram username as input from user
usrname=input("Username:  ")

#Fetching the details of provided useraname using instaloder object
profile=instaloader.Profile.from_username(ig.context, usrname)

# Printing the fetched details and storing the profile pic of that account
print("Username: ", profile.username)
print("Number of Posts Uploaded: ", profile.mediacount)
print(profile.username+" has " + str(profile.followers)+' followers')
print(profile.username+" is following " + str(profile.followees)+' pages/people')
print("Bio: ", profile.biography)
instaloader.Instaloader().download_profile(usrname,profile_pic_only=True)