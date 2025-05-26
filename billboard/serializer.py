from .models import Contact
from rest_framework import serializers


# Create your tests here.
class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Contact
        fields=("name","email")
