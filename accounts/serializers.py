
from rest_framework import serializers
from django.contrib.auth.models import User

# User = get_user_model()


class Userserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name','email')
