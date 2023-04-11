from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework import serializers

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        user_id = self.context['request'].user.id
        adv_list = Advertisement.objects.filter(creator=user_id, status='OPEN').count()
        if (self.context['request'].method == 'POST' or data.get('status') == 'OPEN') and adv_list > 9:
            raise ValidationError('Нельзя иметь более 10 открытых объявлений')
        return data
