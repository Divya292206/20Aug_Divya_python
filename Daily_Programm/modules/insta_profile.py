import instaloader

instaId = "mr_tushar_pariya"

L = instaloader.Instaloader()

L.download_profile(instaId, profile_pic_only=False)

print("Profile Pic Downloaded Successfully")