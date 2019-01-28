from django.shortcuts import render

from rest_framework.response import Response

# Create your views here.

from picontrol.control import read_pin, read_all_pin, write_pin_value, write_pin_mode
from pins.pagination import PaginationAPIView
from pins.serializers import PinSerializer

class PinView(PaginationAPIView):
    serializer_class = PinSerializer

    def get(self, request, pin=None):
        if pin:
            pin = int(pin)
            response = read_pin(pin)

            return Response(data=response)
        else:
            queryset = read_all_pin()
            page = self.paginate_queryset(queryset)
            if page is not None:
                return self.get_paginated_response(page)

            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)

    def post(self, request, pin=None):
        if not pin:
            return Response({"physical": "No pin number."})

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        mode = serializer.validated_data.pop("mode", None)
        value = serializer.validated_data.pop("value", None)
        physical = serializer.validated_data.pop("physical")

        if mode is None and value is None:
            response = {"operation": False, "pin": read_pin(physical)}
            return Response(data=response)

        if mode is not None:
            response = write_pin_mode(physical, mode)

        if value is not None:
            response = write_pin_value(physical, value)
        data = {"operation": True, "pin": response}
        return Response(data=data)

