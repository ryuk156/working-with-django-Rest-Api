from rest_framework import serializers
from .models import Post

class Postserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Post
        fields = '__all__'
        extra_fields = ['title','content']