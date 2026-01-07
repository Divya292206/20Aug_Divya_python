from rest_framework import serializers
from myapp.models import userinfo   

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = userinfo
        fields = '__all__'