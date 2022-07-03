from django.core import serializers
feom . import models


data = serializers.serialize("xml", SomeModel.objects.all())

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = “__all__”