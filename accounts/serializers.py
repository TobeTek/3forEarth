"""
Tobe created unique serializers to automatically handle sorting users into categories sponsor, company.
Not using built in allauth
"""

from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()

class SponsorSerializer(serializers.ModelSerializer):
    password= serializers.CharField(write_only = True)
    
    def create(self,validated_data):
        user = UserModel(**validated_data)
        user.set_password(validated_data['password'])
        user.is_sponsor = True
        user.save()
        return user

    class Meta:
        model = UserModel
        fields = ('id','first_name','last_name','username','email','password')
        write_only_fields = ('password',)
        read_only_fields = ('id',)
    
class CompanySerializer(serializers.ModelSerializer):
    password= serializers.CharField(write_only = True)
    
    def create(self,validated_data):
        user = UserModel(**validated_data)
        user.set_password(validated_data['password'])
        user.is_company = True
        user.save()
        return user

    class Meta:
        model = UserModel
        fields = ('id','first_name','last_name','username','email','password')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

