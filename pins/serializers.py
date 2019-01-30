from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework import serializers

class PinSerializer(serializers.Serializer):
    physical = serializers.IntegerField(
        label="Pin Physical Number",
        validators=[MaxValueValidator(40), MinValueValidator(1)],
        read_only=True,
    )

    hr_mode = serializers.CharField(
        max_length=12,
        label="Human Readable Pin Mode",
        read_only=True,
        allow_null=True, allow_blank=True
    )

    hr_value = serializers.CharField(
        max_length=4,
        label="Human Readable Pin Value",
        read_only=True,
        allow_null=True, allow_blank=True
    )

    mode = serializers.IntegerField(
        validators=[MaxValueValidator(1), MinValueValidator(0)],
        label="Pin Mode",
        required=False
    )

    name = serializers.CharField(
        max_length=7,
        label="Pin Name",
        read_only=True
    )

    value = serializers.IntegerField(
        label="Pin Value",
        required=False
    )

    BCM = serializers.IntegerField(
        label="Pin BCM Number",
        read_only=True,
        allow_null=True
    )

    is_gpio = serializers.BooleanField(
        read_only=True,
        label="Is pin gpio?"
    )
