# -*- coding: utf-8 -*-
from rest_framework import serializers
from testapp.modules.testmodule.models.example_model import ExampleModel


class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = '__all__'
