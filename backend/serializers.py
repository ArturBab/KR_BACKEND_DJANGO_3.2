from backend.models import *
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
   # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Article
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'username',
                  'email', 'password', 'is_superuser']
        extra_kwargs = {'password': {
            'write_only': True
        }}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance
