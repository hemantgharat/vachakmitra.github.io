from rest_framework import serializers
from .models import Story_Details

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story_Details
        fields = ['_id','story_title','story_level','story_image','story_para']