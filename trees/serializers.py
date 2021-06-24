from rest_framework import serializers
from .models import Tree, TreeType

class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = ('id','tree_type','date_created','date_planted','height','in_flower','latitude','longtitude','sponsor','planted')

class TreeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreeType
        fields = ('id','tree_picture','flower_picture','common_name','latin_name','max_height','max_age','company','price',)