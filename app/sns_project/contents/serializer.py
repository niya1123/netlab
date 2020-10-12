from rest_framework import serializers

from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question_title', 'choice1', 'choice2', 'choice3', 'choice4',
        'answer', 'content')