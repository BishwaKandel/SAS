from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import check_password, make_password
from django.utils.crypto import get_random_string


class HRManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HRManager
        fields = ('id', 'ManagerID', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = HRManager
        fields = ('ManagerID', 'username', 'email', 'password')

    def create(self, validated_data):
        # If ManagerID is not in validated_data, generate a unique one
        manager_id = validated_data.get('ManagerID') or self.generate_unique_manager_id()

        # Add the generated ManagerID to validated_data
        validated_data['ManagerID'] = manager_id

        # Create the HRManager user with the ManagerID
        hr_manager = HRManager.objects.create_user(
            validated_data['ManagerID'],
            validated_data['email'],
            validated_data['username'],
            validated_data['password'],
        )

        return hr_manager

    def generate_unique_manager_id(self):
        # Generate a 4-digit ManagerID
        while True:
            manager_id = get_random_string(length=4, allowed_chars='0123456789')
            # Check if the generated ManagerID already exists in the database
            if not HRManager.objects.filter(ManagerID=manager_id).exists():
                return manager_id

class LoginSerializer(serializers.Serializer):
    ManagerID = serializers.CharField(required = True)
    password = serializers.CharField(required = True, write_only = True)



class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = self.context['request'].user
        if not check_password(data['old_password'], user.password):
            raise serializers.ValidationError({"old_password": "Old password is incorrect."})
        if data['old_password'] == data['new_password']:
            raise serializers.ValidationError({"new_password": "New password must be different from the old password."})
        return data

    def save(self, **kwargs):
        user = self.context['request'].user
        user.password = make_password(self.validated_data['new_password'])
        user.save()
        return user


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    new_password = serializers.CharField(write_only=True)

    def validate_email(self, value):
        if not HRManager.objects.filter(email=value).exists():
            raise serializers.ValidationError("No account found with this email.")
        return value

    def create(self, validated_data):
        """Create method to satisfy DRF requirement"""
        user = HRManager.objects.get(email=validated_data["email"])
        user.password = make_password(validated_data["new_password"])
        user.save()
        return user