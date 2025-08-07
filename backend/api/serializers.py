from rest_framework import serializers

class ScanRequestSerializer(serializers.Serializer):
    url = serializers.URLField()
    headers = serializers.DictField(child=serializers.CharField(), required=False)

class ScanResultSerializer(serializers.Serializer):
    vulnerability = serializers.CharField()
    risk = serializers.ChoiceField(choices=['low', 'medium', 'high'])
    details = serializers.CharField() 