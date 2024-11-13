from rest_framework import serializers
from exam.models import Course

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields = ['course_name', 'question_number', 'total_marks']