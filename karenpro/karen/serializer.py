from rest_framework import serializers
from .models import questions

class getquestion(serializers.ModelSerializer):
    class Meta():
        model = questions
        fields = (
            'Question',
            'Sound'
            )
        
