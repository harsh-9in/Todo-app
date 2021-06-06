from rest_framework import serializers
from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ['id', 'first_name','last_name','roles', 'email','password']
        extra_kwargs = {
            ' password':
            {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        user = models.UserProfile.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            role=validated_data['roles'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        return user
