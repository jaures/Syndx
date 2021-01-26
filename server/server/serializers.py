from django.contrib.auth.models import User, Group
from . models import UserProfile, Place, Post, GeoPost, BeaconPost, Vote
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['uuid','profile_img','user']

class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['uuid','name','lat','lng','postal_code','place_id']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['uuid','created_on','updated_on','content','media_url']

class GeoPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeoPost
        fields = ['uuid','created_on','updated_on','parent','content','media_url', 'location']

class BeaconPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeoPost
        fields = ['uuid','created_on','updated_on','parent','content','media_url', 'location', 'start','duration']

class VoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['uuid','vote','user','post']