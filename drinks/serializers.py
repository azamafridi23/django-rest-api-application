'''
In Django, serializers.py is a file used to define serializers, which are a crucial part of the Django REST framework (DRF). Serializers in DRF allow complex data types, 
such as querysets and model instances, to be converted into Python data types like dictionaries, lists, and primitive data types. These serialized representations can 
then be rendered into various content types like JSON or XML, which are suitable for transmitting over the internet.

The primary purpose of serializers.py is to provide a structured way to define how data should be converted into JSON or other formats when building APIs. It serves two main functions:

Serialization: It transforms complex data types, like Django model instances or querysets, into Python data types, making it easier to convert them into JSON or other formats for API responses.

Deserialization: It also handles the reverse process, where incoming data (typically in JSON format) is converted into complex data types, like model instances, to be processed or saved in the database.


'''


from rest_framework import serializers
from .models import Drink


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id','name','description']