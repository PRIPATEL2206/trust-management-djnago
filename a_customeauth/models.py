from django.db import models
from django.contrib.auth.models import User

BASE_PROFILE_UPLOAD = "profiles/"

def get_upload_url(profile,filename:str):
    return BASE_PROFILE_UPLOAD + str(profile.user.id) + "." + filename.split('.')[-1]


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    avatar = models.ImageField(upload_to=get_upload_url,null=True)

    def get_avatar_url(self):
        return self.avatar.url if self.avatar else '/media/profiles/defult_profile_image.jpg'
    def __str__(self):
        return self.user.username
    
     