from django.db import models
from django.contrib.auth.models import User
import uuid


class UserProfile(models.Model):
    '''
    Base Model to hold all User data
    '''
    uuid = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    profile_img = models.URLField()

    class Meta:
        ordering = ['user']
        def __unicode__(self):
            return self.title

class Place(models.Model):
    '''
    Base Model to hold Location data
    '''
    uuid = models.UUIDField(unique=True)
    name = models.CharField(max_length=128)
    lat = models.FloatField()
    lng = models.FloatField()
    postal_code = models.SlugField(max_length=16)
    # Google Places Database ID
    place_id = models.TextField()
    
    class Meta:
        ordering = ['name']
        def __unicode__(self):
            return self.title

class Post(models.Model):
    '''
    Base Model for holding Post Information
    '''
    uuid = models.UUIDField(unique=True)
    created_on = models.DateTimeField(auto_now_add=True, auto_created=True)
    updated_on = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey(to='self', on_delete=models.CASCADE, default='')
    content = models.TextField()
    media_url = models.URLField()

    class Meta:
        ordering = ['created_on']
        def __unicode__(self):
            return self.title


class GeoPost(Post):
    '''
    Post with Location Data
    '''
    location = models.ForeignKey(to=Place, on_delete=models.CASCADE)

class BeaconPost(GeoPost):
    '''
    GeoPost for a time Datetime and duration Data
    '''
    start = models.DateTimeField()
    duration = models.DurationField()

class Vote(models.Model):
    '''
    Base Model for Holding User Votes 
    '''
    uuid = models.UUIDField(unique=True)
    vote = models.BooleanField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['user']
        def __unicode__(self):
            return self.title