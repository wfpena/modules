# -*- coding: utf-8 -*-
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from testapp.modules.testmodule.api.serializers import ExampleSerializer
from testapp.modules.testmodule.models.example_model import ExampleModel


class ExampleViewSet(ModelViewSet):
    serializer_class = ExampleSerializer
    queryset = ExampleModel.objects.all()

    @list_route(methods=('get',))
    def get_users(self, request, format=None):
        example_resp = ExampleModel.objects.all()
        return Response(self.serializer_class(example_resp, many=True).data)

