from rest_framework import serializers

from .models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = "__all__"

    def create(self, validated_data):
        resume = Resume.objects.create(**validated_data)
        return resume

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.speciality = validated_data.get(
            'speciality', instance.speciality)
        instance.grade = validated_data.get('grade', instance.grade)
        instance.education = validated_data.get(
            'education', instance.education)
        instance.experience = validated_data.get(
            'experience', instance.experience)
        instance.portfolio = validated_data.get(
            'portfolio', instance.portfolio)
        instance.title = validated_data.get('title', instance.title)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['owner'] = instance.owner.username
        return representation
