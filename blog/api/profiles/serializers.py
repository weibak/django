from rest_framework import serializers

from profiles.models import Profile


class ProfileModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "age", "image", "status", "created_at"]
