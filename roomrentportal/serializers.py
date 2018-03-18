from rest_framework import serializers
from .models import UserModel

class UserSerializer(serializers.Serializer):
    class meta:
        model=UserModel
        feilds=('name','email','password','contact_no')
